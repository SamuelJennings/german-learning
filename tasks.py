import datetime

from invoke import task


@task
def build(c, live=False):
    """
    Build the documentation
    """
    if live:
        c.run("sphinx-autobuild -b html --watch docs -c docs docs docs/_build/html --open-browser --port 5000")
    else:
        c.run("sphinx-build -E -b html docs docs/_build")


@task
def release(c):
    """
    Release a new version of the app using year.release-number versioning.
    """
    # 1. Determine the current year
    current_year = datetime.datetime.now().year

    # # 3. Form the new version string
    year, num = c.run("poetry version -s", hide=True).stdout.strip().split(".")
    year = int(year)
    num = int(num)
    version = f"{current_year}.1" if year != current_year else f"{year}.{num + 1}"

    # # 4. Update the version in pyproject.toml
    c.run(f"poetry version {version}")

    # # 5. Commit the change
    c.run(f'git commit pyproject.toml -m "release v{version}"')

    # # 6. Create a tag and push it
    c.run(f'git tag -a v{version} -m "Release {version}"')
    c.run("git push --tags")
    c.run("git push origin main")

