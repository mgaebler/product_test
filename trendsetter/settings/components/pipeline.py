# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'common': {
        'source_filenames': (
            'sass-bootstrap/lib/bootstrap.scss',
            'sass-bootstrap/dist/css/bootstrap-theme.css',
        ),
        'output_filename': 'css/common.css',
        'extra_context': {'media': 'screen,projection'},
    },
    'app': {
        'source_filenames': ('app/sass/*.sass',),
        'output_filename': 'css/app.css',
        'extra_context': {'media': 'screen,projection'},
    }
}

PIPELINE_JS = {
    'common': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'sass-bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/common.js',
    }
}


PIPELINE_COMPASS_BINARY = '/usr/bin/env compass'   # default: '/usr/bin/env compass'
# PIPELINE_COMPASS_ARGUMENTS = '-c path/to/config.rb'  # default: ''
PIPELINE_COMPILERS = (
    'pipeline_compass.compass.CompassCompiler',
)

# PIPELINE_COMPILERS = (
#     'pipeline.compilers.sass.SASSCompiler',
# )

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'