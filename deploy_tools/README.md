## Deployment steps
1. Run `./deploy_tools/deploy_staging` to deploy to the staging server.

2. Run `./test_dev` to test the staging server against the test suite.

3. Assuming the tests passed in step 2, run `./deploy_tools/deploy_live` to deploy to the live server. You will need to confirm you want to deploy to production.

4. Double-check that the changes were successful by visiting the site.

## Provisioning
[Obey the Testing Goat](https://www.obeythetestinggoat.com/book/chapter_making_deployment_production_ready.html).

1. Make sure the following software is installed: Python 3, pip, git, and nginx.

2. Optional: Use [certbot](https://certbot.eff.org/) to set up HTTPS.

3. Clone this repository in `/srv/dev.django-showcase.haverford.edu`.

4. Symlink `/srv/dev.django-showcase.haverford.edu/deploy_tools/nginx-dev-conf` to `/etc/nginx/sites-available/showcase-dev`, and symlink that to `/etc/nginx/sites-enabled/showcase-dev`.

5. Run `sudo systemctl reload nginx` to restart nginx.

6. Symlink `/srv/dev.django-showcase.haverford.edu/deploy_tools/gunicorn-dev.django-showcase.haverford.edu.service` to `/etc/systemd/system/` (keeping the same name).

7. Run `sudo systemctl daemon-reload`.

8. Run `sudo systemcl enable gunicorn-dev.django-showcase.haverford.edu.service`.

9. Run `sudo systemcl start gunicorn-dev.django-showcase.haverford.edu.service`.

10. Repeat steps 3-9 replacing `dev.django-showcase.haverford.edu` with `django-showcase.haverford.edu`.

You can view the Systemd logs with `sudo journalctl -u gunicorn-showcase.service`.
