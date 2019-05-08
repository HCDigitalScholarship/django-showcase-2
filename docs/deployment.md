# Deployment
Deployment is the process of getting your code from your personal computer to the server that actually runs the public website. In this project, we have two servers: a staging server for verifying that our changes work, and a production server which serves the public site (in actual fact, the staging and production versions of the site run on the same physical server, but the two sites are completely separate from one another).

Deployment is really easy! Just follow these steps:

1. Run `./deploy <user>`, where `<user>` is your user account on the server, to deploy to the staging server, run the test suite, and deploy to the live server if it passes. If you get an error for `Fatal error: run() received nonzero return code 128 while executing!`, then you probably forgot to push your code to GitHub.

2. Double-check that the changes were successful by visiting the site.
