import logging
import subprocess
import copy
from datetime import datetime

import ucloud.version


logger = logging.getLogger(__name__)


def shell(cmd):
    print(cmd)
    p = subprocess.check_output(cmd)
    return p.decode().strip()


class Bumper:
    def __init__(self, version):
        self.version = version
        versioned = version.split('.')
        if len(versioned) != 3:
            raise ValueError('invalid version {}'.format(version))

        major, minor, patch = versioned
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)

    def bump_major(self):
        clone = copy.deepcopy(self)
        clone.major += 1
        clone.minor = 0
        clone.patch = 0
        return clone

    def bump_minor(self):
        clone = copy.deepcopy(self)
        clone.minor += 1
        clone.patch = 0
        return clone

    def bump_patch(self):
        clone = copy.deepcopy(self)
        clone.patch += 1
        return clone


class StepWriteChangelog:
    classifier_tokens = ['FEATURES', 'ENHANCEMENTS', 'BUG FIXES']

    def __init__(self, changelog_file='CHANGELOG.md', is_prerelease=True, is_dry_run=True):
        self.state = ''
        self.logs = {}
        self.changelog_file = changelog_file
        self.is_prerelease = is_prerelease
        self.is_dry_run = is_dry_run

    @staticmethod
    def get_git_logs():
        version = shell('git describe --tags --abbrev=0')
        commit_sha = shell('git show-ref -s {}'.format(version))
        return shell('git log --format=%B {}..HEAD'.format(commit_sha))

    def get_change_logs(self):
        logs = {}
        for line in self.get_git_logs().split('\n'):
            line = line.strip()
            if not line:
                continue

            if line.strip(':') in self.classifier_tokens:
                self.state = line
                logs.setdefault(line, [])
                continue

            if line.startswith('- ') and self.state:
                logs[self.state].append(line)
            else:
                logger.warning('ignore changelog: {}'.format(line))

        return logs

    def write_changelog(self, logs):
        buffer_lines = []
        should_bump = None

        # render change logs
        for i, token in enumerate(self.classifier_tokens):
            items = logs.get(token)
            if not items:
                continue

            buffer_lines.append(token)
            for item in items:
                buffer_lines.append('- ' + item)

            if should_bump is None:
                should_bump = i

        if should_bump is None:
            logger.warning('no content should be release')
            # raise ValueError('no content should be release')

        # auto increase version number
        bumper = Bumper(ucloud.version.version)
        if should_bump == 0:
            if not self.is_prerelease:
                bumper = bumper.bump_major()
            else:
                bumper = bumper.bump_minor()
        elif should_bump == 1:
            bumper = bumper.bump_minor()
        else:
            bumper = bumper.bump_patch()

        if not self.is_dry_run:
            # insert change logs at the begin of changelog file
            with open('CHANGELOG.md', 'r+') as f:
                content = f.read()
                f.seek(0)
                f.write('\n\n'.join([
                    '## {} ({})'.format(bumper.version, datetime.now().date().isoformat()),
                    '\n'.join(buffer_lines),
                    content,
                ]))

        return bumper.version

    def write_version(self, version):
        version_code = 'version = "{}"'.format(version)
        if self.is_dry_run:
            print(version_code)
            return

        with open('./ucloud/version.py', 'w') as f:
            f.write(version_code)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--changelog-file', default='CHANGELOG.md',
                        help='the file path of changelog file')
    parser.add_argument('--production', default=False, action='store_true', help='is prerelease')
    parser.add_argument('--dry-run', default=False, action='store_true', help='is dry run')

    args = parser.parse_args()
    print(args)

    step1 = StepWriteChangelog(
        changelog_file=args.changelog_file,
        is_dry_run=args.dry_run,
        is_prerelease=not args.production,
    )
    logs = step1.get_change_logs()
    version = step1.write_changelog(logs)
    step1.write_version(version)


if __name__ == '__main__':
    main()
