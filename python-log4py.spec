
%define		module	log4py

Summary:	Python logging module
Summary(pl.UTF-8):	Moduły Pythona do obsługi logowania zdarzeń
Name:		python-%{module}
Version:	1.3
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/log4py/%{module}-%{version}.tar.gz
# Source0-md5:	dc250a8a899c7e70464d683dfc3bdc4f
URL:		http://www.its4you.at/log4py.php
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4Py is a Python logging module similar to log4j. It supports
logging to files or to stdout/stderr, variable log-levels,
configurable output formats and configuration via configuration files.

%description -l pl.UTF-8
Log4Py jest modułem języka Python, podobnym do log4j. Moduł umożliwia
logowanie zdarzeń do plików, na standardowe wyjście oraz standardowe
wyjście błędów, tworzenie różnych poziomów logowania, konfigurowanie
wyświetlanych informacji oraz konfigurację za pomocą plików
konfiguracyjnych.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitescriptdir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ChangeLog,AUTHORS,LICENSE} readme.txt log4py.conf doc/html
%{py_sitescriptdir}/*.py[co]
