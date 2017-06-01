Name: aerospike-client-c@EVENTNAME@
Version: @VERSION@
Release: 1%{?dist}
Summary: Aerospike C Client Shared Library@EVENTDESC@
License: Proprietary
Group: Development/Libraries
BuildArch: x86_64
Vendor: Aerospike, Inc.

%description
The Aerospike C client is used to connect with an Aerospike server and perform database operations.

%define __spec_install_post /usr/lib/rpm/brp-compress

%files
%defattr(-,root,root)
/usr/lib/libaerospike.so
%defattr(-,aerospike,aerospike)
/opt/aerospike/client

%pre
if ! id -g aerospike >/dev/null 2>&1; then
	echo "Adding group aerospike"
	/usr/sbin/groupadd -r aerospike
fi
if ! id -u aerospike >/dev/null 2>&1; then
	echo "Adding user aerospike"
	/usr/sbin/useradd -d /opt/aerospike -c 'Aerospike' -g aerospike aerospike
fi

%post
/sbin/ldconfig
