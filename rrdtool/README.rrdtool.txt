First line is a newer content.
Second line added while in staging area.
Adding new branch details
Steps 1 through 5 have to be done as root user:

On CentOS 7.x:

1. Install epel (on RHEL7, this corresponds to epel-release-7-8.noarch
   or later version of RPM).

2. Type "yum repolist" to update as well as view the repository list.

3. Type "yum install python-pip" to install pip package (pip stands for
   python installation package).

4. Type "pip install Flask" to install "Flask" Python software

5. Then, make sure the following are installed, since these are the dependent
   packages that are required to configure rrdtool:
   - glib2-devel
   - pcre-devel (glib2-devel installs pcre-devel as a dependency)
   - libpng-devel
   - zlib-devel (libpng-devel installs zlib-devel as a dependency)
   - pango-devel (this installs 22 dependent pkgs that are needed by rrdtool)
   - libxml2-devel (this also installs xz-devel as a dependency)
   - perl-ExtUtils-MakeMaker (installs 8 dependent pkgs including perl-devel)

On Ubuntu 16.04 LTS:

1. Install python-pip
   # apt-get install python-pip

2-4: Type "pip install Flask" to install "Flask" Python software

On Ubuntu 18.04 LTS:

1. Install python3-pip
   # apt-get install python3-pip

2-4: Type "pip3 install Flask" to install "Flask" Python software

Common to both Ubuntu 16.04 LTS and Ubuntu 18.04 LTS:

5. Then, make sure the following are installed, since these are the dependent
   packages that are required to configure rrdtool:
   - libglib2.0-dev
   - libpcre3-dev (libglib2-dev installs this a dependency)
     (# apt-get install libglib2.0-dev)
   - libpng-dev
     (# apt-get install libpng-dev)
   (- zlib1g-dev is usually installed as part of default Ubuntu install)
   - libpango1.0-dev
     (# apt-get install libpango1.0-dev)
   - libxml2-dev
     (# apt-get install libxml2-dev)
   - libextutils-makemaker-cpanfile-perl
     (# apt-get install libextutils-makemaker-cpanfile-perl)

Common to both CentOS 7.x and Ubuntu (16.04 LTS and 18.04 LTS):

6. Do the following as ordinary user:
   cd <workdir>/acceloprime/pkg/tools/ui/rrdtool-1.7.0
   ./configure

7. After a successful configure is done, do a make:
   make

8. Once "make" succeeds, start caching software as root user:
   su
   qsconfig_new start

9. In another terminal/screen, do the following as an ordinary user:
   cd <workdir>/acceloprime/pkg/tools/ui/ap_dashboard_v1
   On CentOS 7.x and Ubuntu 16.04 LTS, invoke:
   python routes.py
   On Ubuntu 18.04 LTS, invoke:
   python3 routes.py

   This starts the web server that serves the requests related to caching
   stats and status.

10. In another terminal/screen, do the following as an ordinary user:
    cd <workdir>/acceloprime/pkg/tools/ui/rrdtool-1.7.0/src
    On CentOS 7.x and Ubuntu 16.04 LTS, invoke:
    python rrdsampler.py
    On Ubuntu 18.04 LTS, invoke:
    python3 rrdsampler.py

11. In your favourite web-browser do the following to connect the client to
    the web server for requests related to caching stats and status.
    - If you are connecting from the local server, enter:
      http://127.0.0.1:5500/
    - If you are connecting from a remote server, enter:
      http://<IP_ADDR_OF_ACCELOPRIME_SOFTWARE_SERVER>:5500/
