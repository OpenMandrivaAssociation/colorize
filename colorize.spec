Name:		colorize
Version:	0.3.4
Release:	2
License:	GPLv2+
Group:		Text tools
URL:		https://www.solbu.net/hoved/english/software.htm
Source0:	http://www.solbu.net/progs/%{name}-%{version}.tar.gz
Summary:	Colorized output from tail, like your log files
BuildArch:	noarch
Requires:	perl

%description
This is a perl script, made by Istvan Karaszi, to colorize' your logs.
You can use your own colors, you can simply modify your configuration file 
in your home directory ($HOME), or system-wide (/etc/colorizerc).

%prep
%setup -q

%build

%install
install -m644 %{name}.1.gz -D %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}rc -D %{buildroot}%{_sysconfdir}/%{name}rc

%files
%doc README THANKS TIPS TODO examples changelog.gz
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat May 07 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.4-1
+ Revision: 671289
- add empty %%build section for consistency and to satisfy rpmlint
- fix mixed-use-of-spaces-and-tabs
- cosmetics
- don't abbreviate 'configuration' with 'config' to satisfy rpmlint
- mark config file as %%config(noreplace)
- indent
- fix incorrect spelling
- remove '.' at end of summary line
- drop copyright file as the license doesn't require to ship it
- cleanups
- remove legacy rpm stuff
- imported package colorize


* Thu Apr 2 2010 Johnny A. Solbu <johnny@solbu.net> 0.3.4-1mdv
- Initial release
