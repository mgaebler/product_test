# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

# PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'common': {
        'source_filenames': (
            # 'sass-bootstrap/dist/css/bootstrap.css',
            'bootstrap-sass-3.3.2/bootstrap-theme.css',
            'lightbox/dist/ekko-lightbox.css',
            'css3-social-signin-buttons.css',
        ),
        'output_filename': 'css/common.css',
        'extra_context': {'media': 'screen,projection'},
    },
    'app': {
        'source_filenames': ('app/app.sass',),
        'output_filename': 'app/app_out.css',
        # 'variant': 'datauri',
        'extra_context': {'media': 'screen,projection'},
    }
}

PIPELINE_JS = {
    'common': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'bootstrap-sass-3.3.2/assets/javascripts/bootstrap.js',
            'lightbox/dist/ekko-lightbox.js',
            'app/app.js',
        ),
        'output_filename': 'js/common.js',
    }
}

PIPELINE_SASS_ARGUMENTS = '--compass --update --trace'

PIPELINE_COMPILERS = (
    'core.contrib.pipeline.compilers.sass.SASSCompiler',
)

# PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

# MANIFESTO_EXCLUDED_MANIFESTS = (
        # 'randomapp.manifest.WrongManifest',
# )
