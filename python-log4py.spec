
%include	/usr/lib/rpm/macros.python

%define		module	log4py

Summary:	Python IRC library
Summary(pl):	Modu�y Pythona do osb�ugi IRC
Name:		python-%{module}
Version:	0.7.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Python
Group(da):	Udvikling/Sprog/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(is):	�r�unart�l/Forritunarm�l/Python
Group(it):	Sviluppo/Linguaggi/Python
Group(ja):	��ȯ/����/Python
Group(no):	Utvikling/Programmeringsspr�k/Python
Group(pl):	Programowanie/J�zyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	����������/�����/Python
Group(sl):	Razvoj/Jeziki/Python
Group(sv):	Utveckling/Spr�k/Python
Group(uk):	��������/����/Python
Source0:	http://prdownloads.sourceforge.net/log4py/%{module}-%{version}.tar.gz
URL:		http://www.its4you.at/log4py.php
BuildRequires:	rpm-pythonprov
%requires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log4Py is a Python logging module similar to log4j. It supports
logging to files or to stdout/stderr, variable log-levels,
configurable output formats and configuration via configuration files.

%description -l pl
Log4Py jest modu�em j�zyka Python, podobnym do log4j. Modu� umo�liwia
logowanie zdarze� do plik�w, na standardowe wyj�cie oraz standardowe
wyj�cie b��d�w, tworzenie r�nych poziom�w logowania, konfigurowanie
wy�wietlanych informacji oraz konfiguracj� za pomoc� plik�w
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

gzip -9nf doc/{ChangeLog,AUTHORS,LICENSE} readme.txt log4py.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/html
%{py_sitedir}/*.py[co]
