<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <!-- <title>[% nodename %] - Proxmox Virtual Environment</title> -->
    <title>[% nodename %] - koyu</title>

    <link rel="icon" sizes="128x128" href="/pve2/images/logo-128.png" />
    <link rel="apple-touch-icon" sizes="128x128" href="/pve2/images/logo-128.png" />
    <link rel="stylesheet" type="text/css" href="/pve2/touch/resources/css/sencha-touch.css" />
    <link rel="stylesheet" type="text/css" href="/pve2/touch/resources/css/pve.css?ver=4578.3.5.4" />
    [% IF langfile %]
    <script type='text/javascript' src='/pve2/locale/pve-lang-zh_CN.js'></script>
    [% ELSE %]
    <script type="text/javascript">function gettext(buf) { return buf; }</script>
    [% END %]
    <script type="text/javascript">
    Proxmox = {
	Setup: { auth_cookie_name: 'PVEAuthCookie' },
	UserName: '[ % username %]',
	CSRFPreventionToken: '[% token %]'
    };
    </script>
    <script type="text/javascript" src="/pve2/touch/sencha-touch-all-debug.js"></script>
    <!-- <script type="text/javascript" src="/proxmoxlib.js?ver=[% wtversion %]"></script> -->
    <script type="text/javascript" src="/proxmoxlib.js?ver=ver=4578.3.5.4"></script>
    <script type="text/javascript" src="/pve2/touch/pvemanager-mobile.js?ver=4578.3.5.4"></script>
    <script type="text/javascript">
if (typeof(PVE) === 'undefined') PVE = {};
    </script>
  </head>
  <body>
  </body>
</html>
