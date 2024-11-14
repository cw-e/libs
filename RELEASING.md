# Release Checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/uhcode/libs/actions) should be running
      cleanly for all merges to `main`.
      [![Test](https://github.com/uhcode/libs/workflows/Test/badge.svg)](https://github.com/uhcode/libs/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/uhcode/libs/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/uhcode/libs/actions/workflows/deploy.yml)
      has deployed to [PyPI](https://pypi.org/project/cwe-libs/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y cwe-libs && pip3 install -U cwe-libs && python3 -c "import cwe-libs; print(cwe-libs.__version__)"
```