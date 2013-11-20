from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
OSCAR_SHOP_NAME = 'Oscar'
OSCAR_SHOP_TAGLINE = ''

# Basket settings
OSCAR_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
OSCAR_BASKET_COOKIE_OPEN = 'oscar_open_basket'
OSCAR_BASKET_COOKIE_SAVED = 'oscar_saved_basket'
OSCAR_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Currency
OSCAR_DEFAULT_CURRENCY = 'GBP'
OSCAR_CURRENCY_LOCALE = 'en_GB'

# Max number of products to keep on the user's history
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20

# Paths
OSCAR_IMAGE_FOLDER = 'images/products/%Y/%m/'
OSCAR_PROMOTION_FOLDER = 'images/promotions/'

# Copy this image from oscar/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
OSCAR_MISSING_IMAGE_URL = 'image_not_found.jpg'
OSCAR_UPLOAD_ROOT = '/tmp'

# Address settings
OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

# Search settings
OSCAR_SEARCH_SUGGEST_LIMIT = 10

# Product list settings
OSCAR_PRODUCTS_PER_PAGE = 20

# Checkout
OSCAR_ALLOW_ANON_CHECKOUT = False

# Partners
OSCAR_PARTNER_WRAPPERS = {}

# Promotions
COUNTDOWN, LIST, SINGLE_PRODUCT, TABBED_BLOCK = (
    'Countdown', 'List', 'SingleProduct', 'TabbedBlock')
OSCAR_PROMOTION_MERCHANDISING_BLOCK_TYPES = (
    (COUNTDOWN, "Vertical list"),
    (LIST, "Horizontal list"),
    (TABBED_BLOCK, "Tabbed block"),
    (SINGLE_PRODUCT, "Single product"),
)
OSCAR_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'))

# Reviews
OSCAR_MODERATE_REVIEWS = False

# Accounts
OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# This enables sending alert notifications/emails
# instantly when products get back in stock
# by listening to stock record update signals
# this might impact performace for large numbers
# stock record updates.
# Alternatively, the management command
# ``oscar_send_alerts`` can be used to
# run periodically, e.g. as a cronjob. In this case
# instant alerts should be disabled.
OSCAR_EAGER_ALERTS = True

# Registration
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'oscar@example.com'

# Offers
OSCAR_OFFER_BLACKLIST_PRODUCT = None

# Cookies
OSCAR_COOKIES_DELETE_ON_LOGOUT = ['oscar_recently_viewed_products', ]

# Hidden Oscar features, e.g. wishlists or reviews
OSCAR_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
OSCAR_DASHBOARD_NAVIGATION = {
    'dashboard': {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
        'position': 0
    },
    'catalogue': {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'position': 1,
        'children': {
            'products': {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
                'position': 0
            },
            'categories': {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
                'position': 1
            },
            'ranges': {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
                'position': 2
            },
            'stock-alerts': {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
                'position': 3
            },
        }
    },
    'fulfilment': {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'position': 2,
        'children': {
            'orders-list': {
                'label': _('Order management'),
                'url_name': 'dashboard:order-list',
                'position': 0
            },
            'order-stats': {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
                'position': 0
            },
            'partners': {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
                'position': 0
            },
        }
    },
    'customers': {
        'label': _('Customers'),
        'icon': 'icon-group',
        'position': 3,
        'children': {
            'users': {
                'label': _('Customer management'),
                'url_name': 'dashboard:users-index',
                'position': 0
            },
            'user-alerts': {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
                'position': 1
            },
        }
    },
    'offers': {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'position': 4,
        'children': {
            'list': {
                'label': _('Offer management'),
                'url_name': 'dashboard:offer-list',
                'position': 0
            },
            'vouchers': {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
                'position': 1
            },
        },
    },
    'content': {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'position': 5,
        'children': {
            'blocks': {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
                'position': 0
            },
            'blocks-by-page': {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
                'position': 1
            },
            'pages': {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
                'position': 2
            },
            'email-templates': {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
                'position': 3
            },
            'reviews': {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
                'position': 4
            },
        }
    },
    'reports': {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
        'position': 6
    },
}
OSCAR_DASHBOARD_NAVIGATION_OVERRIDES = {}
# Search facets
OSCAR_SEARCH_FACETS = {
    'fields': {
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        'category': {
            'name': _('Category'),
            'field': 'category'
        }
    },
    'queries': {
        'price_range': {
            'name': _('Price range'),
            'field': 'price',
            'queries': [
                # This is a list of (name, query) tuples where the name will
                # be displayed on the front-end.
                (_('0 to 40'), '[0 TO 20]'),
                (_('20 to 40'), '[20 TO 40]'),
                (_('40 to 60'), '[40 TO 60]'),
                (_('60+'), '[60 TO *]'),
            ]
        }
    }
}

OSCAR_SETTINGS = dict(
    [(k, v) for k, v in locals().items() if k.startswith('OSCAR_')])
