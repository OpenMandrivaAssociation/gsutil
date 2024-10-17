Summary:	A utility to save, restore and reboot Grandstream Budgetone phones
Name:		gsutil
Version:	3.0
Release:	6
License:	GPL
Group:		System/Servers
URL:		https://www.pkts.ca/gsutil.shtml
Source:		http://www.pkts.ca/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A utility to dump and restore the configuration of the Grandstream Budgetone
VOIP telephone, up to and including version 1.0.6.7 of the firmware.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 gsutil %{buildroot}%{_bindir}/gsutil

%clean
rm -r %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc README Changelog gxp2000.template.txt
%attr(0755,root,root) %{_bindir}/gsutil


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-5mdv2011.0
+ Revision: 619281
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.0-4mdv2010.0
+ Revision: 429332
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.0-3mdv2009.0
+ Revision: 246667
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.0-1mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 3.0-1mdv2008.0
+ Revision: 66664
- Import gsutil



* Fri Jul 28 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0-1mdk
- 3.0

* Fri Feb 03 2006 Jerome Soyer <saispo@mandriva.org> 2.3-1mdk
- New release 2.3

* Thu Dec 22 2005 Oden Eriksson <oeriksson@mandriva.com> 2.2-1mdk
- initial Mandriva package

* Sat Sep 10 2005 Charles Howes <gsutil@ch.pkts.ca> 2.2-1
- Minor tweak from Frank Scholz to support ATA-286 fully

* Thu Aug 18 2005 Charles Howes <gsutil@ch.pkts.ca> 2.1-1
- Actually check to see if the password was correct... Doh!

* Sat Jul 30 2005 Charles Howes <gsutil@ch.pkts.ca> 2.0-1
- Made it work for 1.0.6.x firmware phones
- Possibly broke the 1.0.5.x firmware code, but maybe not; untested.

* Wed Jul 27 2005 Charles Howes <gsutil@ch.pkts.ca> 1.2-1
- added version check, print
- added GS format

* Mon Jul 12 2005 Charles Howes <gsutil@ch.pkts.ca> 1.1-1
- check hostname before processing

* Sat Jul  9 2005 Charles Howes <gsutil@ch.pkts.ca> 1.0-1
- initial build
