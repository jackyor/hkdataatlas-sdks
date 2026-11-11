# Release setup

The npm package and PyPI distribution are both named `hkdataatlas`. Confirm names, ownership, version and package contents before the first release. A package name or these instructions do not establish registry availability.

## Accounts and permissions

1. Create or sign in to a [GitHub account](https://github.com/), and arrange permission to create and administer the intended repository and its Actions environments. The provisional repository is `jackyor/hkdataatlas-sdks`; confirm the owner and name before configuring trust.
2. [Create an npm account](https://docs.npmjs.com/creating-a-new-npm-user-account/), verify its email and enable [two-factor authentication](https://docs.npmjs.com/configuring-two-factor-authentication/). The npm package is unscoped and needs no organization. Your npm login can differ from the package name; confirm the package name is available and that your account may publish it.
3. [Create a PyPI account](https://pypi.org/account/register/), verify its email and enable [two-factor authentication](https://docs.pypi.org/account-management/2fa/). Check the distribution name and arrange project ownership or publishing permissions.
4. Keep passwords, recovery codes, verification codes and API tokens out of issues, chat and the repository. Each maintainer uses their own account.

## Trusted publishing

Use separate GitHub Actions environments restricted to the intended release tags or branches, and job-scoped `id-token: write` for releases. No required reviewer gate is assumed. Match each registry's trusted publisher to the exact GitHub owner `jackyor`, repository `hkdataatlas-sdks`, workflow filename `release.yml` and its configured environment (`npm` or `pypi`); confirm these values against the actual repository before setup. Restrict release tags and environment access to the intended identities. The release job downloads the built and checked artifacts; it does not regenerate different artifacts during publication.

For a new PyPI project, add a [pending trusted publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) in the account's Publishing settings. It does not reserve the project name: first successful publication creates the project. For an existing project, its owner configures the trusted publisher in project settings. The [PyPI GitHub OIDC guide](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-pypi) explains the job permission and publishing action.

For npm, the documented [trusted publisher setup](https://docs.npmjs.com/trusted-publishers/) starts in an existing package's settings. An authorized initial publication bootstraps a new unscoped package; then configure the trusted publisher for subsequent releases. This first publication is a registry release. Local token credentials may be used for bootstrap while npm permits direct token publishing. That ability is scheduled to end in January 2027, so hosted OIDC remains the primary automatic release path; the workflow does not require a token or a staged manual approval flow. The unscoped package is public. The trusted release requires a GitHub-hosted runner, Node 22.14.0 or later, npm 11.5.1 or later, and a `repository.url` matching the GitHub repository. Choose the direct publish permission if the workflow uses `npm publish`. A new trust configuration expires unless it has a first successful trusted publish within two days, so configure it when that publish is ready. After setup, restrict token-based publishing as appropriate. Do not create or paste a long-lived registry token for this workflow.

## Release procedure

From the exact candidate source, run public generation, synthetic response and package checks and Dagger CI; optional live response checks are not a release requirement; compare artifacts to the candidate and inspect package contents and source attribution. Record the revision and results. Initial publication waits for account and trusted-publisher readiness and release authorization. Confirm registry trust and names, then trigger the release workflow. Verify the published versions, provenance where available, and installation/imports from both registries. Publication is a separate action from preparing or testing this repository.
