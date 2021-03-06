# Provisioning
Provisioning is the process of setting up this website to run on a new server. Provisioning is an advanced task which only needs to be done very infrequently, so unless you know what you're doing you should check out the deployment guide at `docs/deployment.md` instead.

These instructions are based on the deployment chapter of [Obey the Testing Goat](https://www.obeythetestinggoat.com/book/chapter_making_deployment_production_ready.html).

You'll need to provision a server running Ubuntu (e.g., from Digital Ocean or AWS), and update the domain name registry to point to the server's IP address.

## Prepare the server
1. Make sure the following software is installed: Python 3, pip, git, and nginx.

2. Make sure your user account is in the `www-data` group by running the following command (note: if you belong to groups other than `sudo` make sure to add them to the comma-separated list):

```
$ sudo usermod -aG sudo,www-data <your-username>
```

3. Create a `sites` directory and make `www-data` the owner:

```
$ sudo mkdir /srv/sites
$ sudo chown www-data: /srv/sites
$ sudo chmod g+w /srv/sites
```

4. Optional: Use [certbot](https://certbot.eff.org/) to set up HTTPS.

## Deploy the code
1. Deploy the code with `./deploy_tools/deploy_staging` (or `./deploy_tools/deploy_prod` the second time around).

2. Symlink `/srv/sites/dev.django-showcase.haverford.edu/deploy_tools/nginx-dev-conf` to `/etc/nginx/sites-available/dev.django-showcase.haverford.edu`, and symlink that to `/etc/nginx/sites-enabled/dev.django-showcase.haverford.edu`.

3. Run `sudo systemctl reload nginx` to restart nginx.

4. Symlink `/srv/sites/dev.django-showcase.haverford.edu/deploy_tools/uwsgi-dev-conf` to `/etc/uwsgi/apps-available/showcase-dev.ini`.

5. Run `sudo service uwsgi restart`.

6. Repeat the steps in this section, replacing `dev.django-showcase.haverford.edu` with `django-showcase.haverford.edu`, and running `./deploy_tools/deploy_prod` in step 1.
