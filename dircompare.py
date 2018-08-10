#!/usr/bin/env python
import filecmp
import pprint
import os
import click
import sys


def dir_compare(dir1, dir2, prefix='.'):
    """Return a recursive dircompare.py comparison report as a dictionary."""

    comparison = filecmp.dircmp(dir1, dir2)

    data = {
        'only_dir1'             : [r'{}/{}'.format(prefix, i) for i in comparison.left_only],
        'only_dir2'             : [r'{}/{}'.format(prefix, i) for i in comparison.right_only],
        'same_name_same_content': [r'{}/{}'.format(prefix, i) for i in comparison.same_files],
        'same_name_diff_content': [r'{}/{}'.format(prefix, i) for i in comparison.diff_files],
    }

    for datalist in data.values():
        datalist.sort()

    if comparison.common_dirs:
        for folder in comparison.common_dirs:
            # Update prefix to include new sub_folder
            prefix += '/' + folder

            # Compare common folder and add results to the report
            sub_dir1 = os.path.join(dir1, folder)
            sub_dir2 = os.path.join(dir2, folder)
            sub_report = dir_compare(sub_dir1, sub_dir2, prefix)

            # Add results from sub_report to main report
            for key, value in sub_report.items():
                data[key] += value

    return data


@click.command()
@click.argument('path1', required=True, type=click.Path(exists=True, resolve_path=True), )
@click.argument('path2', required=True, type=click.Path(exists=True, resolve_path=True), )
def main(path1, path2):
    """
    A little tool that will compare files in two directories of your choice.
    Provide the paths to the directories.
    Here is an example:
    path1 = '/home/lina/split_record'
    path2 = '/home/lina/split_record_mono'
    """
    if path1 == path2:
        click.echo(click.style("You provided the same path for both dirs - nothing to compare", fg='red'))

    else:
        print "Let's compare {0} and {1}".format(path1, path2)
        try:
            result = dir_compare(path1, path2)
            pprint.pprint(result)

        except OSError:
            click.echo(click.style('Found a file with permission denied - exiting', fg='red'))
            pass


if __name__ == '__main__':
    sys.exit(main())
