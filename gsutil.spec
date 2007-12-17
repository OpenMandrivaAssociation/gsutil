Summary:	A utility to save, restore and reboot Grandstream Budgetone phones
Name:		gsutil
Version:	3.0
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
URL:		http://www.pkts.ca/gsutil.shtml
Source:		http://www.pkts.ca/%{name}-%{version}.tar.bz2
BuildArch:	noarch

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
