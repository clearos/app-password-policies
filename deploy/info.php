<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'password_policies';
$app['version'] = '2.1.0';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('password_policies_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('password_policies_app_name');
$app['category'] = lang('base_category_system');
$app['subcategory'] = lang('base_subcategory_account_manager');

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['requires'] = array(
    'app-accounts',
    'app-groups',
    'app-users',
);

$app['core_requires'] = array(
    'app-openldap-core',
);

$app['core_file_manifest'] = array(
    'accounts-event'=> array(
        'target' => '/var/clearos/events/accounts/password_policies',
        'mode' => '0755'
    ),
    'password-policies-synchronize' => array(
        'target' => '/usr/sbin/password-policies-synchronize',
        'mode' => '0755',
        'owner' => 'root',
        'group' => 'root',
    )
);
