
Name: app-password-policies
Epoch: 1
Version: 1.1.0
Release: 1%{dist}
Summary: Password Policies
License: GPLv3
Group: ClearOS/Apps
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: %{name}-core = 1:%{version}-%{release}
Requires: app-base
Requires: app-accounts
Requires: app-groups
Requires: app-users

%description
The Password Policy module adds functionality to the directory server to enforce password creation rules.  This enforces users to create passwords that meet your criteria and helps to make your system more secure.

%package core
Summary: Password Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Requires: app-base-core
Requires: app-openldap-core

%description core
The Password Policy module adds functionality to the directory server to enforce password creation rules.  This enforces users to create passwords that meet your criteria and helps to make your system more secure.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/password_policies
cp -r * %{buildroot}/usr/clearos/apps/password_policies/

install -D -m 0755 packaging/password-policies-synchronize %{buildroot}/usr/sbin/password-policies-synchronize

%post
logger -p local6.notice -t installer 'app-password-policies - installing'

%post core
logger -p local6.notice -t installer 'app-password-policies-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/password_policies/deploy/install ] && /usr/clearos/apps/password_policies/deploy/install
fi

[ -x /usr/clearos/apps/password_policies/deploy/upgrade ] && /usr/clearos/apps/password_policies/deploy/upgrade

exit 0

%preun
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-password-policies - uninstalling'
fi

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-password-policies-core - uninstalling'
    [ -x /usr/clearos/apps/password_policies/deploy/uninstall ] && /usr/clearos/apps/password_policies/deploy/uninstall
fi

exit 0

%files
%defattr(-,root,root)
/usr/clearos/apps/password_policies/controllers
/usr/clearos/apps/password_policies/htdocs
/usr/clearos/apps/password_policies/views

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/password_policies/packaging
%exclude /usr/clearos/apps/password_policies/tests
%dir /usr/clearos/apps/password_policies
/usr/clearos/apps/password_policies/deploy
/usr/clearos/apps/password_policies/language
/usr/clearos/apps/password_policies/libraries
/usr/sbin/password-policies-synchronize
