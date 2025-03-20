Name:           mybatop
Version:        2.0.0
Release:        1%{?dist}
Summary:        A battery monitoring tool

License:        GPLv3
URL:            https://github.com/vishnumur777/mybatop
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash
Requires:       systemd
Requires:       dmidecode
Requires:       python3
Requires:       python3-pandas
Requires:       python3-plotly


%description
mybatop continuously monitors laptop battery status
and provides detailed analytics through HTML reports.

%prep
%setup -q

%install
mkdir -p %{buildroot}/opt/mybatop
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}/usr/bin

cp -r * %{buildroot}/opt/mybatop/
rm -rf %{buildroot}/opt/mybatop/filesystemd/
cp filesystemd/* %{buildroot}/etc/systemd/system/
ln -s /opt/mybatop/scripts/runscript/mybatop %{buildroot}/usr/bin/mybatop


%post
chmod -R +rwx /opt/mybatop
systemctl daemon-reload
systemctl enable --now mybatop-shutdown.service
systemctl enable --now mybatop-startup.service
systemctl enable --now mybatop-status.service

%files
%dir /opt/mybatop
/opt/mybatop/*
/etc/systemd/system/mybatop-*.service
/usr/bin/mybatop

%changelog
* Wed Mar 19 2025 Varun M <varunushamurali@gmail.com> - 2.0.0-1
- Initial package
