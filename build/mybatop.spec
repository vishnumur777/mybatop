Name:           mybatop
Version:        "$APP_VERSION"
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
mkdir -p %{buildroot}/opt/mybatop/data
touch %{buildroot}/opt/mybatop/data/temporaryfiler.n
rm -rf %{buildroot}/opt/mybatop/filesystemd/
cp filesystemd/* %{buildroot}/etc/systemd/system/
ln -s /opt/mybatop/scripts/runscript/mybatop %{buildroot}/usr/bin/mybatop


%post
chmod -R +rx /opt/mybatop
if [ -n "$SUDO_USER" ] && [ "$SUDO_USER" != "root" ]; then
    chown -R $SUDO_USER:$SUDO_USER /opt/mybatop
elif [ -n "$PKEXEC_UID" ]; then
    ACTUAL_USER=$(getent passwd "$PKEXEC_UID" | cut -d: -f1)
    chown -R $ACTUAL_USER:$ACTUAL_USER /opt/mybatop
else
    # Fallback: find first non-root user with UID >= 1000
    ACTUAL_USER=$(getent passwd | awk -F: '$3 >= 1000 && $3 < 65534 {print $1; exit}')
    if [ -n "$ACTUAL_USER" ]; then
        chown -R $ACTUAL_USER:$ACTUAL_USER /opt/mybatop
    fi
fi
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
