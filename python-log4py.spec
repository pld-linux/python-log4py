%include	/usr/lib/rpm/macros.python

%define		module	log4py

Summary:	Python logging module
Summary(pl):	Modu³y Pythona do obs³ugi logowania zdarzeñ
Name:		python-%{module}
Version:	0.7.1
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/log4py/%{module}-%{version}.tar.gz
URL:		http://www.its4you.at/log4py.php
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4Py is a Python logging module similar to log4j. It supports
logging to files or to stdout/stderr, variable log-levels,
configurable output formats and configuration via configuration files.

%description -l pl
Log4Py jest modu³em jêzyka Python, podobnym do log4j. Modu³ umo¿liwia
logowanie zdarzeñ do plików, na standardowe wyj¶cie oraz standardowe
wyj¶cie b³êdów, tworzenie ró¿nych poziomów logowania, konfigurowanie
wy¶wietlanych informacji oraz konfiguracjê za pomoc± plików
konfiguracyjnych.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ChangeLog,AUTHORS,LICENSE} readme.txt log4py.conf doc/html
%{py_sitedir}/*.py[co]
