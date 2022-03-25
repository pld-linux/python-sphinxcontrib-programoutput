#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to include program output
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do załączania wyjścia programu
Name:		python-sphinxcontrib-programoutput
Version:	0.17
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-programoutput/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-programoutput/sphinxcontrib-programoutput-%{version}.tar.gz
# Source0-md5:	7bad912b0af6bb504819659ffe382199
URL:		https://pypi.org/project/sphinxcontrib-programoutput/
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.7.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.7.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples up
to date.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do dokładnego wstawiania wyjścia dowolnych
poleceń do dokumentów. Pozwala utrzymywać aktualność przykładów
poleceń.

%package -n python3-sphinxcontrib-programoutput
Summary:	Sphinx extension to include program output
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do załączania wyjścia programu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-sphinxcontrib-programoutput
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples up
to date.

%description -n python3-sphinxcontrib-programoutput -l pl.UTF-8
Rozszerzenie Sphinksa do dokładnego wstawiania wyjścia dowolnych
poleceń do dokumentów. Pozwala utrzymywać aktualność przykładów
poleceń.

%package apidocs
Summary:	API documentation for Python sphinxcontrib-programoutput module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib-programoutput
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib-programoutput module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib-programoutput.

%prep
%setup -q -n sphinxcontrib-programoutput-%{version}

%build
%if %{with python2}
LC_ALL=C.UTF-8 \
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
sphinx-build -b html doc doc/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
# XXX: shared dir
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/programoutput
%{py_sitescriptdir}/sphinxcontrib_programoutput-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_programoutput-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-programoutput
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
# XXX: shared dir
%dir %{py3_sitescriptdir}/sphinxcontrib
%{py3_sitescriptdir}/sphinxcontrib/programoutput
%{py3_sitescriptdir}/sphinxcontrib_programoutput-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_programoutput-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
