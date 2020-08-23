--- make/configure.py.orig	2020-01-04 19:28:06.000000000 +0300
+++ make/configure.py	2020-03-19 06:51:06.935220000 +0300
@@ -1409,11 +1409,11 @@
     grp.add_argument( '--enable-ffmpeg-aac', dest="enable_ffmpeg_aac", default=not host_tuple.match( '*-*-darwin*' ), action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-ffmpeg-aac', dest="enable_ffmpeg_aac", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
-    h = IfHost( 'Nvidia NVENC video encoder', '*-*-linux*', '*-*-mingw*', none=argparse.SUPPRESS).value
-    grp.add_argument( '--enable-nvenc', dest="enable_nvenc", default=IfHost( True, '*-*-linux*', '*-*-mingw*', none=False).value, action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
+    h = IfHost( 'Nvidia NVENC video encoder', '*-*-linux*', '*-*-freebsd*', '*-*-mingw*', none=argparse.SUPPRESS).value
+    grp.add_argument( '--enable-nvenc', dest="enable_nvenc", default=IfHost( True, '*-*-linux*', '*-*-freebsd*', '*-*-mingw*', none=False).value, action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-nvenc', dest="enable_nvenc", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
-    h = IfHost( 'Intel QSV video encoder/decoder', '*-*-linux*', '*-*-mingw*', none=argparse.SUPPRESS).value
+    h = IfHost( 'Intel QSV video encoder/decoder', '*-*-linux*', '*-*-freebsd*', '*-*-mingw*', none=argparse.SUPPRESS).value
     grp.add_argument( '--enable-qsv', dest="enable_qsv", default=IfHost(True, "*-*-mingw*", none=False).value, action='store_true', help=(( 'enable %s' %h ) if h != argparse.SUPPRESS else h) )
     grp.add_argument( '--disable-qsv', dest="enable_qsv", action='store_false', help=(( 'disable %s' %h ) if h != argparse.SUPPRESS else h) )
 
@@ -1677,14 +1677,14 @@
     options.enable_gtk_mingw  = IfHost(options.enable_gtk_mingw, '*-*-mingw*',
                                        none=False).value
     # Disable NVENC on unsupported platforms
-    options.enable_nvenc      = IfHost(options.enable_nvenc, '*-*-linux*',
+    options.enable_nvenc      = IfHost(options.enable_nvenc, '*-*-linux*', '*-*-freebsd*',
                                        '*-*-mingw*', none=False).value
     # NUMA is linux only and only needed with x265
     options.enable_numa       = (IfHost(options.enable_numa, '*-*-linux*',
                                         none=False).value
                                  and options.enable_x265)
     # Disable QSV on unsupported platforms
-    options.enable_qsv        = IfHost(options.enable_qsv, '*-*-linux*',
+    options.enable_qsv        = IfHost(options.enable_qsv, '*-*-linux*', '*-*-freebsd*',
                                        '*-*-mingw*', none=False).value
     # Disable VCE on unsupported platforms
     options.enable_vce        = IfHost(options.enable_vce, '*-*-linux*', '*-*-mingw*',
@@ -2124,7 +2124,7 @@
     stdout.write( 'Enable NVENC:       %s' % options.enable_nvenc )
     stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
     stdout.write( 'Enable QSV:         %s' % options.enable_qsv )
-    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
+    stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'freebsd' or host_tuple.system == 'mingw') else stdout.write( '\n' )
     stdout.write( 'Enable VCE:         %s' % options.enable_vce )
     stdout.write( ' (%s)\n' % note_unsupported ) if not (host_tuple.system == 'linux' or host_tuple.system == 'mingw') else stdout.write( '\n' )
 
