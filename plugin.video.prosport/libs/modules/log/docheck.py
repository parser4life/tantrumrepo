#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Sports Hub
# Addon id: plugin.video.prosport
# Addon Provider: MuadDib

'''
This check has been put in place to stop the inclusion of TVA (and friends) addons in builds
from build makers. Why? Because they are greedy bastards that worry only about the money and not about
the community or users. Regardles of what they say, that is what they speear to be for. Therefore I do
not want this addon running along side their own.
                                                                                           - MuadDib/Tantrum
'''

def ttvcheck(uninstall=False, bypass=False):
    if bypass:
        return
    import hashlib
    import xbmcvfs
    import xbmc
    bad_md5s = [
        ('special://home/media/splash.png', '926dc482183da52644e08658f4bf80e8'),
        ('special://home/media/splash.png', '084e2bc2ce2bf099ce273aabe331b02e')]
    bad_addons = ['plugin.program.indigo', 'repository.exodus', 'repository.kodil', 'repository.tva.common']

    found_md5 = False

    for path, bad_md5 in bad_md5s:
        f = xbmcvfs.File(path)
        md5 = hashlib.md5(f.read()).hexdigest()
        if md5 == bad_md5:
            found_md5 = True
            break

    has_bad_addon = any(xbmc.getCondVisibility('System.HasAddon(%s)' % (addon)) for addon in bad_addons)
    if has_bad_addon or found_md5:
        import xbmcgui
        import sys
        line2 = 'Press OK to uninstall this addon' if uninstall else 'Press OK to exit this addon'
        xbmcgui.Dialog().ok('Incompatible System', 'This addon will not work with the build you have installed', line2)
        if uninstall:
            import xbmcaddon
            import shutil
            addon_path = xbmcaddon.Addon().getAddonInfo('path').decode('utf-8')
            shutil.rmtree(addon_path)
        sys.exit()