Follow these instructions to add your own personal webpage to the interns app.

1. Make sure you've followed the one-time set-up steps in `README.md`, and read the section on "How to work on this repository."
2. Create a new template at `interns/templates/interns/<you>.html` where `<you>` is your Haverford username (without the angle brackets). You can base your template off `interns/templates/interns/iafisher.html`, but feel free to customize it however you like!
3. Add a link to your page on the main interns page at `interns/templates/interns/index.html`.
4. Add the URL to your page at `interns/urls.py`. The path should be your Haverford username again.
5. Write a view for your page in `interns/views.py`.
6. Write a unit test\* for your page in `interns/tests.py`.
7. Write a functional test for your page in `test/test_interns.py`.
8. Run `./test_local` to make sure your tests pass.
9. Commit your changes, push them to your own branch (**not** to `master`) on GitHub, and [submit a pull request](https://github.com/HCDigitalScholarship/ds-cookbook/blob/master/code_review.md).
10. Once your pull request is approved, merge your branch into `master` and follow the steps in `deploy_tools/README.md` to deploy your code into production!

\*: I'm using terminology a bit loosely here: normally a unit test checks a single component of the application, while a functional test checks the behavior of all the components of the app working together. What I'm calling unit tests are not strictly unit tests, because they involve multiple components (e.g, URL routing, views, templates). Nonetheless, they are still different from functional tests because our functional tests involve spinning up an actual browser, rendering the HTML and CSS, and running the JavaScript, which our unit tests do not do.
