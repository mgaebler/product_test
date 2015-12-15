# django pipeline default configuration
## http://django-pipeline.readthedocs.org/en/latest/configuration.html

# PIPELINE_ENABLED = False

PIPELINE_CSS = {
    'app': {
        'source_filenames': (
            'lightbox/dist/ekko-lightbox.css',
            'app/css/app.css',
        ),
        'output_filename': 'common.css',
        'extra_context': {'media': 'screen,projection'},
    }
}

PIPELINE_JS = {
    'common': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'jquery-lazy/jquery.lazy.js',
            'bootstrap-sass-3.3.2/assets/javascripts/bootstrap.js',
            'lightbox/dist/ekko-lightbox.js',
            'wysihtml-0.4.17/dist/wysihtml5x.js',
            'wysihtml-0.4.17/dist/wysihtml5x-toolbar.js',
            'wysihtml-0.4.17/parser_rules/advanced_and_extended.js',
            'app/app.js',
        ),
        'output_filename': 'js/common.js',
    }
}


# PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

#
# I choose the noop compressor for js since the other fail in different ways
#
# JSMIN compiles, but fails by loosing script code at the end.
#
# Yuglify fails with parse error.
# JS_Parse_Error (/usr/lib/node_modules/yuglify/node_modules/uglify-js/lib/parse-js.js:263:18)

# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

# MANIFESTO_EXCLUDED_MANIFESTS = (
        # 'randomapp.manifest.WrongManifest',
# )
