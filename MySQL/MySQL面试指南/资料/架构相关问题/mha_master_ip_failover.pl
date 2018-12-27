#!/usr/bin/env perl

use strict;
use warnings FATAL => 'all';

use Getopt::Long;

my (
    $command, $orig_master_host, $orig_master_ip,$ssh_user,
    $orig_master_port, $new_master_host, $new_master_ip,$new_master_port,
    $orig_master_ssh_port,$new_master_ssh_port,$new_master_user,$new_master_password
);

my $vip = '#vip#/24';
my $key = '1';
my $ssh_start_vip = "sudo /sbin/ifconfig eth0:$key $vip";
my $ssh_stop_vip = "sudo /sbin/ifconfig eth0:$key down";
my $ssh_Bcast_arp= "sudo /sbin/arping -I bond0 -c 3 -A #vip#";

GetOptions(
    'command=s'          => \$command,
    'ssh_user=s'         => \$ssh_user,
    'orig_master_host=s' => \$orig_master_host,
    'orig_master_ip=s'   => \$orig_master_ip,
    'orig_master_port=i' => \$orig_master_port,
    'orig_master_ssh_port=i' => \$orig_master_ssh_port,
    'new_master_host=s'  => \$new_master_host,
    'new_master_ip=s'    => \$new_master_ip,
    'new_master_port=i'  => \$new_master_port,
    'new_master_ssh_port' => \$new_master_ssh_port,
    'new_master_user' => \$new_master_user,
    'new_master_password' => \$new_master_password

);

exit &main();

sub main {
    $ssh_user = defined $ssh_user ? $ssh_user : 'root';
    print "\n\nIN SCRIPT TEST====$ssh_user|$ssh_stop_vip==$ssh_user|$ssh_start_vip===\n\n";

    if ( $command eq "stop" || $command eq "stopssh" ) {

        my $exit_code = 1;
        eval {
            print "Disabling the VIP on old master: $orig_master_host \n";
            &stop_vip();
            $exit_code = 0;
        };
        if ($@) {
            warn "Got Error: $@\n";
            exit $exit_code;
        }
        exit $exit_code;
    }
    elsif ( $command eq "start" ) {

        my $exit_code = 10;
        eval {
            print "Enabling the VIP - $vip on the new master - $new_master_host \n";
            &start_vip();
	    &start_arp();
            $exit_code = 0;
        };
        if ($@) {
            warn $@;
            exit $exit_code;
        }
        exit $exit_code;
    }
    elsif ( $command eq "status" ) {
        print "Checking the Status of the script.. OK \n";
        exit 0;
    }
    else {
        &usage();
        exit 1;
    }
}

sub start_vip() {
    `ssh $ssh_user\@$new_master_host \" $ssh_start_vip \"`;
}
sub stop_vip() {
    `ssh $ssh_user\@$orig_master_host \" $ssh_stop_vip \"`;
}

sub start_arp() {
    `ssh $ssh_user\@$new_master_host \" $ssh_Bcast_arp \"`;
}
sub usage {
    print
    "Usage: master_ip_failover --command=start|stop|stopssh|status --ssh_user=user --orig_master_host=host --orig_master_ip=ip --orig_master_port=port --new_master_host=host --new_master_ip=ip --new_master_port=port\n";
}