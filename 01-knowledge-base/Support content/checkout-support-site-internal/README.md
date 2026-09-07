# Checkout.com support site

We follow docs-as-code practices to create and maintain content on the Checkout.com support site.

To get started:

1. Clone the `checkout-support-site-internal` [repository](https://github.com/cko-web/checkout-support-site-internal).
2. Install the CKO Tech Writing VS Code extension (`cko-tech-writing-extension/cko-tech-writing.vsix`) from the `tech-writers` [repository](https://github.com/cko-web/tech-writers).

---

## Authentication

Calls to the Zendesk API are authenticated using Zendesk credentials tied to the following user: **Sebastian Garcia Cardona**.

Credentials are included in the project as GitHub environment secrets:

- `ZENDESK_EMAIL` - The email address the user uses to sign in to Zendesk.
- `ZENDESK_API_KEY` - The API key generated on Zendesk by the user.
- `ZENDESK_BASE_URL` - Set to `https://checkout1360.zendesk.com` by default. Do not modify.

---

## Branches

Our setup relies on automated syncs to our base branch. As `main` has branch protection rules that prevent this, and because we do not deploy any asset via `main`, we always work directly off of the `staging` branch.

Branch and pull request creation is handled automatically via the exposed editor options.

---

## Project structure

The `Support articles` folder in the project contains all currently published support site content, organised in a folder structure that mirrors the website’s information architecture.

![Project structure](/.assets/images/Project-structure.png)

Each article is a single markdown file (`index.md`) containing support article metadata in the front matter, followed by the article body.

![Support article example](/.assets/images/Support-article-example.png)

---

## Content syncing

The project is set up to automatically sync content from Zendesk to the project’s `staging` branch every day at 7AM. Before you start working on a change, make sure you pull the latest changes to `staging`.

> The `sync-support-articles.py` script in the project exposes an on-demand sync option, but we shouldn’t need to use this in our regular process.

---

## Find an article

To locate a specific article, you can either:

- Navigate down the directory tree, if you know where it sits in the information architecture.
- Search by title in your IDE, if you know the article’s title.
- Search by article ID in your code editor, if you know the article’s ID.

> An article’s parent folder contains both its title and ID.

---

## Update an article

To update an article:

1. Ensure you’re on the `staging` branch.
2. Locate the article you need to modify.
3. Make the necessary content changes.
   If you want the changes to be public, ensure `draft` is set to `false` (this is the default value).

4. Save the file.
5. In the editor, select the _Push changes to Zendesk_ icon located above the file contents.
   This option automatically creates a new branch that branches off of `staging` and raises a new pull request (PR) against `staging`. The pull request description is auto-populated with the modified support article’s data.

   ![The editor-level _Push changes to Zendesk_ option](/.assets/images/Editor-level-push-changes-to-zendesk.png)

6. Once your PR has been reviewed, merge it in.
   This will automatically push your changes to Zendesk.

> This option only creates a PR for the file currently open in the editor. For bulk changes, follow the **Update articles in bulk** process.

---

## Update articles in bulk

To update articles in bulk (for example, if you need to modify site-wide taxonomy via the label-names front matter values):

1. Ensure you’re on the `staging` branch.
2. Locate the first article you need to modify.
3. Make the necessary changes.
  If you want the changes to be public, ensure draft is set to false (this is the default value).

4. Save the file.
5. Repeat steps 2 to 4 for each file that needs changes.
6. In the editor’s project directory, right-click the _Support articles_ folder and select _Push changes to Zendesk_.

   ![The directory-level _Push changes to Zendesk_ option](/.assets/images/Directory-level-push-changes-to-zendesk.png)

   > You must use the _Push changes to Zendesk_ option from the project directory for bulk changes.

   This option automatically creates a new branch that branches off of `staging` and raises a new PR against `staging`. The pull request description is auto-populated with the modified support articles' data.

7. Once your PR has been reviewed, merge it in.
   This will automatically push your changes to Zendesk.

---

## Create a new article

To create a new article:

1. Ensure you’re on the `staging` branch.
2. Use the editor’s left navigation to locate the section folder you want to add an article to.
3. Right-click the section folder and select _Create new support article here_.

   ![The directory-level _Create new support article here_ option](/.assets/images/Create-new-support-article.png)

   This adds a new section folder to the left navigation, with a new `index.md` file within it.

4. Open the file.
   The file contains a support article template. You must provide a title in the front matter, and an article body.

   ![Support article template](/.assets/images/Support-article-template.png)

   Ignore other values, they are auto-populated at a later step.

5. Make the necessary content changes.
   If you want the changes to be public, ensure `draft` is set to `false` (this is the default value).

6. Save the file.
7. In the editor, select the _Push changes to Zendesk_ icon.

   ![The editor-level _Push changes to Zendesk_ option](/.assets/images/Editor-level-push-changes-to-zendesk.png)

   This option automatically creates a new branch that branches off of `staging` and raises a new PR against `staging`. The pull request description is auto-populated with the modified support article’s data.

8. Once your PR has been reviewed, merge it in.
   This will automatically push your changes to Zendesk.
   The automation also writes back the article’s metadata to the file’s front matter, and updates the support article’s parent folder name in the project directory.

---

## Archive an article

> Archiving an article hides it from the public site but does not remove it entirely from Zendesk’s content database. To delete an article, use Zendesk via the browser. You cannot delete an article via the API.

To archive an article:

1. Ensure you’re on the `staging` branch.
2. Locate the article you need to archive.
3. In the file’s front matter, set the `archive` value to `true`.
4. Save the file.
5. In the editor, select the _Push changes to Zendesk_ icon.

   ![The editor-level _Push changes to Zendesk_ option](/.assets/images/Editor-level-push-changes-to-zendesk.png)

   This option automatically creates a new branch that branches off of `staging` and raises a new PR against `staging`. The pull request description is auto-populated with the modified support article’s data.

6. Once your PR has been reviewed, merge it in.
   This will automatically push your changes to Zendesk.
   The file and its parent folder will be removed from the project directory in the next scheduled content sync.
