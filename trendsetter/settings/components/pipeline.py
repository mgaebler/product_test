# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
          'css/core.css',
          'css/colors/*.css',
          'css/layers.css'
        ),
        'output_filename': 'css/colors.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'js/jquery.js',
            'js/d3.js',
            'js/collections/*.js',
            'js/application.js',
        ),
        'output_filename': 'js/stats.js',
    }
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)