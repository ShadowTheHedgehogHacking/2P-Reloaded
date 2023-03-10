#!/usr/bin/python
# This Python file uses the following encoding: utf-8

# Written in Python v2.7.12 by DRGN of SmashBoards (Daniel R. Cappel).
version = 4.4
#4.4.1 last tested version - dreamsyntax
# Find the official thread here for usage and other documentation: 
# http://smashboards.com/threads/melee-code-manager-easily-add-codes-to-your-game.416437/
from collections import OrderedDict


# The value below affects the Code Offset Converter in the Tools tab. If set to False, the search will be much slower, but 
# will also have a little better chance of finding a match.
quickSearch = True

# globalFontSize can set the default size of the program's font, even apart from your system's (OS dependant) settings.
# Negative values indicate pixel size, while positive values are standard font points.
globalFontSize = -12

# So far, the value below is only used for determining a default revision when adding new code changes for a mod in the Mod Construction tab.
# You should also have a DOL by this revision in the Original DOLs folder to add such code changes to a mod.
defaultRevision = 'NTSC 1.02' # Should follow the revision string convention of "[region] [version]"

# The following will ensure that the mod "Enable OSReport Print on Crash" is always installed in your game, as
# long as it's also found in your Mods Library. Change this to False if you don't want this behavior.
alwaysEnableCrashReports = False

# Below are hex ranges that indicate safe areas (free space) for custom code. Between each set of parenthesis, you have the start of a region, followed 
# by the end of that region. You may add new regions, as long as you follow the same formatting that you see here.
#
# (I recommend making a copy of this file or the line(s) you modify, in case you make a mistake or
# would like to undo it later. Then, you can just comment out the back-up line(s) by preceding it with a '#'.)
#
# Remember that each entry needs to be followed by a comma, except for the last one.
# If you'd like to remove all of these regions, you still need to preserve the variable here;
# just make it equal to an empty pair of brackets, i.e. "commonCodeRegions = {}"
#
# You may also add regions. Just be sure that you know what you're doing and have tested the region, and that no regions overlap with one another!
customCodeRegions = OrderedDict([
    ( 'NTSC 1.06|Gen Regions', [ ( 0x4AC, 0x23E0 ) ] ), # Total space: 0x1F34
	# The regions in this first list are the same between all game revisions, hence "ALL" specified for the code region.
	( 'ALL|Common Code Regions', [ ( 0x2C8, 0x398 ), ( 0x39C, 0x498 ), ( 0x4E4, 0x598 ), ( 0x5CC, 0x698 ),			# 0xD0,  0xFC,  0xB4, 0xCC 	= 0x34C
								 ( 0x6CC, 0x798 ), ( 0x8CC, 0x998 ), ( 0x99C, 0xA98 ), ( 0xACC, 0xB98 ),			# 0xCC,  0xCC,  0xFC, 0xCC 	= 0x360
								 ( 0xBCC, 0xE98 ), ( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), (0x10CC, 0x1198 ),			# 0x2CC, 0xCC,  0xCC, 0xCC 	= 0x530
								 ( 0x1220, 0x1298 ), ( 0x1308, 0x1398 ), ( 0x1408, 0x1498 ), ( 0x1508, 0x1598 ),	# 0x78,  0x90,  0x90, 0x90 	= 0x228
								 ( 0x15F0, 0x1698 ), ( 0x16CC, 0x1898 ), ( 0x18CC, 0x1998 ), ( 0x19CC, 0x1E98 ),	# 0xA8,  0x1CC, 0xCC, 0x4CC = 0x80C
								 ( 0x1ECC, 0x1F98 ), ( 0x1FCC, 0x2098 ), ( 0x20CC, 0x2198 ) ] ),					# 0xCC,  0xCC,  0xCC 		= 0x264
																														# Total space of above:  0x1874 Bytes

	( 'NTSC 1.02|20XXHP 4.07 Regions', [ ( 0x18DCC0, 0x197B30 ), 		# Tournament Mode Region 	(0x9E70)
									#	 ( 0x32B96C, 0x32C208 ),		# Area 4 of USB/MCC 		(0x89C)		< Can be included if you remove the PAL FSM List
										 ( 0x32C998, 0x332834 ), 		# Extra USB/MCC Region 		(0x5E9C)
										 ( 0x39063C, 0x3907F4 ),		# Area 5 of USB/MCC 		(0x1B8)
										 ( 0x407540, 0x408F00 ), ] ),	# Aux Code Regions 			(0x19C0)
																				# Total space = 0x11884 Bytes (Or 0x12120 if you add Area 4 of MCC)

																								#______________
	( 'NTSC 1.02|20XXHP 5.0 Regions', [ ( 0x39C, 0x498 ), ( 0x8CC, 0x998 ), ( 0x9CC, 0xA98 ),		#          \
										( 0xECC, 0xF98 ), ( 0xFCC, 0x1098 ), ( 0x1308, 0x1398 ),	  #         \_____ Subset of Common Code Regions (0x87C bytes)
										( 0x1508, 0x1598 ), ( 0x15CC, 0x1698 ), ( 0x18CC, 0x1998 ),	    #       |
										( 0x1ECC, 0x1F98 ), ( 0x20CC, 0x2198 ),					#______________|
										( 0x18DCC0, 0x197B30 ), 				# Tournament Mode Region 	(0x9E70)
										( 0x32BA70, 0x32C208 ),					# Most of Area 4 of USB/MCC (0x798)
	 									( 0x32C998, 0x332834 ), 				# Extra USB/MCC Region 		(0x5E9C)
										#( 0x39063C, 0x3907F4 ), ] ),			# Area 5 of USB/MCC 		(0x1B8)
										( 0x39063C, 0x39078C ), ] ), 			# Area 5 of USB/MCC 		(0x150) # Ended early for space for codes with static location
																						# Total space = 0x10E70 Bytes

	# The following regions are used for the multiplayer tournament mode (which of course will no longer be functional if you use this space). 
	# If you use this space, you may want to add a code that prevents people from accessing this mode so that the game doesn't crash when someone tries to use it.
	( 'NTSC 1.02|Tournament Mode Region, P1', [ ( 0x18DCC0, 0x18E8C0 ) ] ), 	# Total space: 0xC00
	( 'NTSC 1.01|Tournament Mode Region, P1', [ ( 0x18D674, 0x18E274 ) ] ), 	# Total space: 0xC00
	( 'NTSC 1.00|Tournament Mode Region, P1', [ ( 0x18CDC0, 0x18D9C0 ) ] ), 	# Total space: 0xC00
	( 'PAL 1.00|Tournament Mode Region, P1', [ ( 0x18E804, 0x18F404 ) ] ), 		# Total space: 0xC00
	# These regions are part of one contiguous space, and are separated here so that the 
	# Aux Code Regions can remain vanilla, allowing use of the "Enable OSReport Print on Crash" code.
	( 'NTSC 1.02|Tournament Mode Region, P2', [ ( 0x18E8C0, 0x197B30 ) ] ), 	# Total space: 0x9270
	( 'NTSC 1.01|Tournament Mode Region, P2', [ ( 0x18E274, 0x1974E4 ) ] ), 	# Total space: 0x9270
	( 'NTSC 1.00|Tournament Mode Region, P2', [ ( 0x18D9C0, 0x196DE4 ) ] ), 	# Total space: 0x9424
	( 'PAL 1.00|Tournament Mode Region, P2', [ ( 0x18F404, 0x1986A0 ) ] ), 		# Total space: 0x929C
	# The tournament mode regions for versions other than 1.02 have not yet been tested. Please let me know the results if you test them.

	# The regions below are for the unused 'USB Screenshot' feature, described here:
	# http://smashboards.com/threads/the-dol-mod-topic.326347/page-11#post-19130116
	# More accurately known as parts of the "MCC Regions" (Dolphin OS Multi-Channel Communication API)
	
	# If these are used for custom code, then the following changes also need to be made: 
	# 0x1a1b64 --> 60000000, 0x1a1c50 --> 60000000 (nops branch links to these regions; these are DOL addresses for v1.02)
	# MCM will handle the nops above for you if these regions are used, so these notes are just mentioned here in case you want to do something manually.
	( 'NTSC 1.02|Screenshot Regions', [ ( 0x22545c, 0x225644 ), ( 0x329428, 0x329640 ), ( 0x32a890, 0x32a9a0 ), ( 0x32b96c, 0x32c208 ), ( 0x39063c, 0x3907f4 ) ] ),
	( 'NTSC 1.01|Screenshot Regions', [ ( 0x224cd4, 0x224ebc ), ( 0x328750, 0x328968 ), ( 0x329bb8, 0x329cc8 ), ( 0x32ac94, 0x32B530 ), ( 0x38f95c, 0x38fb14 ) ] ),
	( 'NTSC 1.00|Screenshot Regions', [ ( 0x22414c, 0x224334 ), ( 0x327b00, 0x327d18 ), ( 0x328f68, 0x329078 ), ( 0x32a044, 0x32A8E0 ), ( 0x38e778, 0x38e930 ) ] ),
	( 'PAL 1.00|Screenshot Regions', [ ( 0x2272cc, 0x2274b4 ), ( 0x329704, 0x32991c ), ( 0x32AB6C, 0x32AC7C ), ( 0x32BC48, 0x32C4E4 ), ( 0x390564, 0x39071c ) ] ),
								# Space:		0x1e8 					0x218 					0x110 					0x89c 					0x1b8 				= 0xF64 Bytes Total

	# The following is commented out because it seems to cause crashing. Perhaps another nop is needed. More testing required.
	# The code here relates to playing MTH files, so if you don't need those, this may work for you.
	# ( 'NTSC 1.02|Screenshot Regions', [ ( 0x32C998, 0x332834 ) ] ), # Total space: 0x5E9C Bytes
	# ( 'NTSC 1.01|Screenshot Regions', [ ( 0x32BCB8, 0x331B54 ) ] ),
	# ( 'NTSC 1.00|Screenshot Regions', [ ( 0x32B068, 0x330F04 ) ] ),
	# ( 'PAL 1.00|Screenshot Regions', [ ( 0x32CC78, 0x332B14 ) ] ),

	# The regions below are used for the game's vanilla Debug Menu, which of course will no longer be functional if you use this space.
	# The Debug Mode itself (DbLevel) may still work to some extent, but you would at least need a new method to enter it.
	( 'NTSC 1.02|Debug Mode Region', [ ( 0x3f7124, 0x3fac20 ) ] ), # Total space: 0x3AFC (same for all game versions)
	( 'NTSC 1.01|Debug Mode Region', [ ( 0x3f6444, 0x3f9f40 ) ] ),
	( 'NTSC 1.00|Debug Mode Region', [ ( 0x3f5294, 0x3f8d90 ) ] ),
	( 'PAL 1.00|Debug Mode Region', [ ( 0x3f7ecc, 0x3fbae8 ) ] ),

	# These are unused areas containing text used for debugging the game, and have been tested to be safe for overwriting.
	# However, they will disable the use of OS Report features, such as in the useful "Enable OSReport Print on Crash" code.
	# CrazyHand places the FSM Engine and FSM Entries directly after this region.
    ( 'NTSC 1.06|Aux Code Regions', [ ( 0x407540, 0x4088B0 ) ] ),
	( 'NTSC 1.02|Aux Code Regions', [ ( 0x407540, 0x4088B0 ) ] ), # Total space: 0x1370
	( 'NTSC 1.01|Aux Code Regions', [ ( 0x406860, 0x407BD0 ) ] ),
	( 'NTSC 1.00|Aux Code Regions', [ ( 0x405580, 0x4068F0 ) ] ),
	( 'PAL 1.00|Aux Code Regions', [ ( 0x408400, 0x409770 ) ] ),

	# The following regions are only for use with extended NTSC 1.02 SSBM DOLs
	# Part 1 of Data Section 8
	( 'NTSC 1.02|Gecko Code Handler Storage', [ ( 0x4385E0, 0x4395E0 ) ] ), # 0x1000
	# Part 2 of Data Section 8
	( 'NTSC 1.02|Gecko Code List Storage', [ ( 0x4395E0, 0x446EE0 ) ] ), # 0xD900

])


# The Gecko hook (set below) intercepts the game's normal execution to point to the Gecko Codehandler with a standard branch.
# Warning: do not change the hook offsets unless you've first fully uninstalled all Gecko codes from your game.
# Otherwise, the old hook will still remain in your game, and your game will not run unless you manually remove it.
#
# If the regions used for the codelist or codehandler are changed, the next time you open the program and game/DOL,
# any previously installed Gecko codes will not be detected (because the program will be looking in the new region for 
# them), however their code will still be present in the same place as they were before. So you will need to reselect
# and save the mods that you'd like to be installed. And if you want the code in the old regions to be retuned the game's
# original/vanilla hex, use the "Restore" buttons found in the Code-Space Options window (located in the Mods Library tab).
# 
# Note that if Gecko codes are used, the codelist/codehandler will be placed at the start of their respective region,
# defined below. As you can see in the customCodeRegions definitions above, a single region may be one contiguous area, 
# or a collection of several areas. However, any region set for the Gecko codelist or codehandler will only use the first 
# area if there are multiple. The extra space left over in that region may still be used for standard injection mod code 
# and/or standalone functions.
geckoConfiguration = {
	'hookOffsets': { 'NTSC 1.06': 0x177B78, 'NTSC 1.02': 0x3738E0, 'NTSC 1.01': 0x372c00, 'NTSC 1.00': 0x371a2c, 'PAL 1.00': 0x3737e4 },
	'codehandlerRegion': 'Gen Regions', # If Gecko codes are used, the codehandler will be placed at the start of this region (must exist in customCodeRegions)
	'codelistRegion': 'Gen Regions' # If Gecko codes are used, the codelist will be placed at the start of this region (must exist in customCodeRegions)
}
# Recommended defaults:
#	Tournament Mode Region, P2 for the codelist, because it is the largest contiguous area
#	Tournament Mode Region, P1 for the codehandler (Aux Code Regions is a good alternative, but you will lose use of the "Enable OSReport Print on Crash" code)

# The following codehandler is a modified version of the one posted and discussed here: http://smashboards.com/threads/ssbm-dol-that-accepts-gecko-codes.403755/
# This is a fallback, and will only be added to the DOL if Gecko Codes are used and codehandler.bin is not found in the root directory.
geckoCodehandler = ('9421FF58900100087C0802A6900100AC7C0000269001000C7C0902A6900100107C0102A690010014BC6100187F2000A6633A2000735AF9FF7F400124D8410098' # 1 line = 64 bytes
					'D86100A03FE080003E80CC00A3944010639500FFB2B440107FA802A63DE0445261EF474E63E718083CC080007CD03378390000003C6000D06063C0DE808F0000'
					'7C03200040820018808F00047C0320004082000C39EF00084800004C7FA803A6B3944010C8410098C86100A07F2000A6800100AC7C0803A68001000C7C0FF120'
					'800100107C0903A6800100147C0103A6B861001880010008382100A84C00012C4E800020806F0000808F000439EF0008710900012F89000039200000546A1F7E'
					'54653F7E746B1000546301FE4082000C54CC000C480000087E0C83782E0500002C0A000141A0002C41A200E42C0A000341A001AC418202502C0A0005418002D4'
					'41A204E02C0A000741A0050C480005F07D8C1A142C050003418200484181006040BEFF842E0500014191002C548A843E419200107C8961AE392900014800000C'
					'7C89632E39290002354AFFFF40A0FFE44BFFFF54558C003A908C00004BFFFF487C892378409E04C83529FFFF418004C07CA978AE7CA961AE4BFFFFF039EF0008'
					'40BEFF2480AFFFF8816FFFFC54B1043E54AA853E54A5273E2E8500014196001041B500147C8961AE480000107C89632E480000087C89612E7C845A147D298A14'
					'354AFFFF4080FFD44BFFFEDC546907FF418200105508F87E710900012F8900002E8500042D8A00055108083C409E0078418D04B87D8C1A14418C000C41940030'
					'4800001C40940010558C003A816C00004800001C558C003CA16C00007C8920F85529843E7D6B48385484043E7F0B204070A90003418200182C09000241820018'
					'4181001C409A002048000018419A00184800001041990010480000084198000861080001408EFE404194FE3C816FFFF8409E0020706C00084182000C710C0001'
					'41820010398B0010518B033648000008556B0716916FFFF84BFFFE0C40BEFE08546916BA546E87FE2D8E00002E05000470AE00032E8E00024194001441960050'
					'7C6407347C847A14480000685465A7FF4182000C7D27482E7C844A14418E00087C8C22142E8E00014196000880840000546367FF4182003C4090000C7C843214'
					'480000307C848214480000285465A7FF4182000C7D27482E7C844A144090000C7CCC212E4BFFFD807E0C212E4BFFFD784090000C7C8623784BFFFD6C7C902378'
					'4BFFFD6454891E78392900402C05000241800048546B500341820014418100084800001041BEFD404800000840BEFD382C0500034181001041A200107DE7482E'
					'4BFFFD247DE7492E7C64073454841A787DEF22144BFFFD1040BEFD0C7CA74A14409200145464043E91E50000908500044BFFFCF4812500042C09000041A2FCE8'
					'3929FFFF9125000481E500004BFFFCD840BEFCD4546B16BA7F475A14813A0000546E67BE419200842E050005409001742E050003409000902E050001546587FF'
					'418200087C8C22142F0E00014092002441B90018419A000C88840000480000F8A0840000480000F080840000480000E85473E53E41B90020419A001099240000'
					'3884000148000018B1240000388400024800000C91240000388400043673FFFF4080FFD44BFFFC40546587FF418200087C84621471C500014182009C7C844A14'
					'48000094546A87BE548E16BA7E677214409200083A6FFFFC809A000081330000714B0001418200087C9A2378714B0002418200107D334B7840B200087E6C9A14'
					'5465673F2C05000940800054480000797C892214480000407C8921D6480000387D242378480000307D242038480000287D242278480000207D24203048000018' 
					'7D242430480000105D24203E480000087D242630909A00004BFFFB8C2C05000A4181FB84C05A0000C07300004182000CEC43102A48000008EC4300B2D05A0000'
					'4BFFFB647D4802A654A51E787D4A2A14809A0000813300007D4803A64E80002040BEFB445469C03E7D8E6378480000354192000C7E312214480000087D292214'
					'5464C43F38A000004182FB1C7D4588AE7D4549AE38A500017C0520004BFFFFEC2E8A0004553136BA2C11003C7E27882E408200087DD1737841960008A2310000'
					'552956BA2C09003C7D27482E408200087DC9737841960008A12900004E8000202C050004408000287C8923787DC3621455CE003C4BFFFFAD7C8420F85484043E'
					'7D2B20387E2420384BFFFBC4546BE43E4BFFFBBC7C9A23785484183840920020409E000C7DE803A64E8000217DE47A1460000000600000004BFFFA6C2E050003'
					'4191005C3CA048007D836214558C003A4092002040BEFA505744003A7C8C2050508501BA506507FE90AC00004BFFFA3840BEFFBC7D2C7850512501BA90AC0000'
					'398C00047D6F2214396BFFFC7D2B6050512501BA90AB00004BFFFF942E050006419200284BFFFB28558C843E5744843E575A043E7C0C20004180FBA87C0CD000'
					'4080FBA04BFFF9E05745FFFE68A50001710300017C0518004182001C511A0FBC6B5A00025745FFFF418200086B5A0001934FFFFC534807FE4BFFF9AC2C0B0000'
					'418201382C050001418200182C050002418200142C050003418200704BFFF94054CC000C5497463E5498C43E5484063E409E00FC56F906317D9A63787F43D214'
					'575A003A418200187EF707747EF700D01F3700023B3900047F59D0502C1700004182001C3B2000007EE903A6A37A00047F79CA783B5A00024200FFF47C18C800'
					'408200AC4BFFFE905108083C409E009C5477B003418100884180008C547E063E1FDE00025497001E6EF880002C1800004082000862F730005498801E1F3E0004'
					'7F19C0503B2000001F5900047F6FD02E7F57D02E3B3900017C17C040418100347C19F000418100147C1AD8004182FFDC3AF700044BFFFFD0806FFFF860630300'
					'906FFFF892EFFFFC7EF0BB784800001C806FFFF860630100906FFFF861080001480000087C9023785464063E1C8400087DE47A144BFFF8704092000C39000000'
					'48000014546906FF546567FE7D084C305517FFFF408200087D082A785485001F418200087CA62B785485801F418200087CB02B784BFFF8300000000000DEADBEEF000000') 
					# Total size: 0x8C4 bytes (4488 characters). The length of this must be aligned to the nearest 4 bytes.


# For the Menu Text Converter:
menuTextDictionary = {

	# Single-Byte Characters
	'1a' : ' ',  '03' : '\n', # Space, and newLine (line break)

	# English numbers & alphabet			Found in Start.dol
	'2000': '0', '2001': '1', '2002': '2', '2003': '3', '2004': '4', '2005': '5', '2006': '6', '2007': '7', '2008': '8', '2009': '9',
	'200a': 'A', '200b': 'B', '200c': 'C', '200d': 'D', '200e': 'E', '200f': 'F', '2010': 'G', '2011': 'H', '2012': 'I', '2013': 'J',
	'2014': 'K', '2015': 'L', '2016': 'M', '2017': 'N', '2018': 'O', '2019': 'P', '201a': 'Q', '201b': 'R', '201c': 'S', '201d': 'T',
	'201e': 'U', '201f': 'V', '2020': 'W', '2021': 'X', '2022': 'Y', '2023': 'Z',
	'2024': 'a', '2025': 'b', '2026': 'c', '2027': 'd', '2028': 'e', '2029': 'f', '202a': 'g', '202b': 'h', '202c': 'i', '202d': 'j',
	'202e': 'k', '202f': 'l', '2030': 'm', '2031': 'n', '2032': 'o', '2033': 'p', '2034': 'q', '2035': 'r', '2036': 's', '2037': 't',
	'2038': 'u', '2039': 'v', '203a': 'w', '203b': 'x', '203c': 'y', '203d': 'z',

	# Japanese Hiragana						Found in Start.dol
	'203e': '???', '203f': '???', '2040': '???', '2041': '???', '2042': '???', '2043': '???', '2044': '???', '2045': '???', '2046': '???', '2047': '???', 
	'2048': '???', '2049': '???', '204a': '???', '204b': '???', '204c': '???', '204d': '???', '204e': '???', '204f': '???', '2050': '???', '2051': '???', 
	'2052': '???', '2053': '???', '2054': '???', '2055': '???', '2056': '???', '2057': '???', '2058': '???', '2059': '???', '205a': '???', '205b': '???', 
	'205c': '???', '205d': '???', '205e': '???', '205f': '???', '2060': '???', '2061': '???', '2062': '???', '2063': '???', '2064': '???', '2065': '???', 
	'2066': '???', '2067': '???', '2068': '???', '2069': '???', '206a': '???', '206b': '???', '206c': '???', '206d': '???', '206e': '???', '206f': '???', 
	'2070': '???', '2071': '???', '2072': '???', '2073': '???', '2074': '???', '2075': '???', '2076': '???', '2077': '???', '2078': '???', '2079': '???', 
	'207a': '???', '207b': '???', '207c': '???', '207d': '???', '207e': '???', '207f': '???', '2080': '???', '2081': '???', '2082': '???', '2083': '???', 
	'2084': '???', '2085': '???', '2086': '???', '2087': '???', '2088': '???', '2089': '???', '208a': '???', '208b': '???', '208c': '???', '208d': '???', 
	'208e': '???',

	# Japanese Katakana						Found in Start.dol
	'208f': '???', '2090': '???', '2091': '???', '2092': '???', '2093': '???', '2094': '???', '2095': '???', '2096': '???', '2097': '???', '2098': '???', 
	'2099': '???', '209a': '???', '209b': '???', '209c': '???', '209d': '???', '209e': '???', '209f': '???', '20a0': '???', '20a1': '???', '20a2': '???', 
	'20a3': '???', '20a4': '???', '20a5': '???', '20a6': '???', '20a7': '???', '20a8': '???', '20a9': '???', '20aa': '???', '20ab': '???', '20ac': '???', 
	'20ad': '???', '20ae': '???', '20af': '???', '20b0': '???', '20b1': '???', '20b2': '???', '20b3': '???', '20b4': '???', '20b5': '???', '20b6': '???', 
	'20b7': '???', '20b8': '???', '20b9': '???', '20ba': '???', '20bb': '???', '20bc': '???', '20bd': '???', '20be': '???', '20bf': '???', '20c0': '???', 
	'20c1': '???', '20c2': '???', '20c3': '???', '20c4': '???', '20c5': '???', '20c6': '???', '20c7': '???', '20c8': '???', '20c9': '???', '20ca': '???', 
	'20cb': '???', '20cc': '???', '20cd': '???', '20ce': '???', '20cf': '???', '20d0': '???', '20d1': '???', '20d2': '???', '20d3': '???', '20d4': '???', 
	'20d5': '???', '20d6': '???', '20d7': '???', '20d8': '???', '20d9': '???', '20da': '???', '20db': '???', '20dc': '???', '20dd': '???', '20de': '???', 
	'20df': '???', '20e0': '???', '20e1': '???', '20e2': '???',

	# Punctuation							Found in Start.dol
	'20e3': '???', '20e4': '???', '20e5': '???', # These are the "ideographic"/Japanese space, comma, and period (the space here is not the same space character found under '1a')
	'20e6': ',', '20e7': '.', '20e8': '???', '20e9': ':', '20ea': ';', '20eb': '?', '20ec': '!', '20ed': '^', '20ee': '_', '20ef': '???', # '20ef' is an "em dash" (U+2014)
	'20f0': '/', '20f1': '~', '20f2': '|', '20f3': "'", '20f4': '"', '20f5': '(', '20f6': ')', '20f7': '[', '20f8': ']', '20f9': '{', 
	'20fa': '}', '20fb': '+', '20fc': '-', '20fd': '??', '20fe': '=', '20ff': '<', '2100': '>', '2101': '??', '2102': '$', '2103': '%', # '20fd' is not simply another x, but a multiplication sign (U+00D7)
	'2104': '#', '2105': '&', '2106': '*', '2107': '@',

	# Japanese Kanji						Group 1, Found in Start.dol
	'2108': '???', '2109': '???', '210a': '???', '210b': '???', '210c': '???', '210d': '???', '210e': '???', '210f': '???', '2110': '???', '2111': '???',
	'2112': '???', '2113': '???', '2114': '???', '2115': '???', '2116': '???', '2117': '???', '2118': '???', '2119': '???', '211a': '???', '211b': '???',
	'211c': '???', '211d': '???', '211e': '???',

	# Misc Items, Set 1						Found in SdMenu.usd				(Only accessible if the game is set to English)
	#'4000': '??', '4001': '???', '4002': '???', '4003': '???', '4004': '???', '4005': '???', '4006': '???', 	# 4002 seems to be a Roman numeral 2

	# Misc Items, Set 2						Found in SdMenu.dat				(Only accessible if the game is set to Japanese)
	'4000': '???', '4001': '???', '4002': '???', '4003': '???', '4004': '???', '4005': '???', '4006': '???', '4007': '???', '4008': '???', '4009': '???', # The corner brackets are quotation marks in East Asian languages

	# Japanese Kanji						Group 2, Found in SdMenu.dat 	(Only accessible if the game is set to Japanese)
	'400a': '???', '400b': '???', '400c': '???', '400d': '???', '400e': '???', '400f': '???', '4010': '???', '4011': '???', '4012': '???', '4013': '???', # 4010 may instead be ???
	'4014': '???', '4015': '???', '4016': '???', '4017': '???', '4018': '???', '4019': '???', '401a': '???', '401b': '???', '401c': '???', '401d': '???',
	'401e': '???', '401f': '???', '4020': '???', '4021': '???', '4022': '???', '4023': '???', '4024': '???', '4025': '???', '4026': '???', '4027': '???',

	'4028': '???', '4029': '???', '402a': '???', '402b': '???', '402c': '???', '402d': '???', '402e': '???', '402f': '???', '4030': '???', '4031': '???',
	'4032': '???', '4033': '???', '4034': '???', '4035': '???', '4036': '???', '4037': '???', '4038': '???', '4039': '???', '403a': '???', '403b': '???',
	'403c': '???', '403d': '???', '403e': '???', '403f': '???', '4040': '???', '4041': '???', '4042': '???', '4043': '???', '4044': '???', '4045': '???',

	'4046': '???', '4047': '???', '4048': '???', '4049': '???', '404a': '???', '404b': '???', '404c': '???', '404d': '???', '404e': '???', '404f': '???',
	'4050': '???', '4051': '???', '4052': '???', '4053': '???', '4054': '???', '4055': '???', '4056': '???', '4057': '???', '4058': '???', '4059': '???',
	'405a': '???', '405b': '???', '405c': '???', '405d': '???', '405e': '???', '405f': '???', '4060': '???', '4061': '???', '4062': '???', '4063': '???',

	'4064': '???', '4065': '???', '4066': '???', '4067': '???', '4068': '???', '4069': '???', '406a': '???', '406b': '???', '406c': '???', '406d': '???',
	'406e': '???', '406f': '???', '4070': '???', '4071': '???', '4072': '???', '4073': '???', '4074': '???', '4075': '???', '4076': '???', '4077': '???',
	'4078': '???', '4079': '???', '407a': '???', '407b': '???', '407c': '???', '407d': '???', '407e': '???', '407f': '???', '4080': '???', '4081': '???',
	
	'4082': '???', '4083': '???', '4084': '???', '4085': '???', '4086': '???', '4087': '???', '4088': '???', '4089': '???', '408a': '???', '408b': '???',
	'408c': '???', '408d': '???', '408e': '???', '408f': '???', '4090': '???', '4091': '???', '4092': '???', '4093': '???', '4094': '???', '4095': '???',
	'4096': '???', '4097': '???', '4098': '???', '4099': '???', '409a': '???', '409b': '???', '409c': '???', '409d': '???', '409e': '???', '409f': '???',
	
	'40a0': '???', '40a1': '???', '40a2': '???', '40a3': '???', '40a4': '???', '40a5': '???', '40a6': '???', '40a7': '???', '40a8': '???', '40a9': '???',
	'40aa': '???', '40ab': '???', '40ac': '???', '40ad': '???', '40ae': '???', '40af': '???', '40b0': '???', '40b1': '???', '40b2': '???', '40b3': '???',
	'40b4': '???', '40b5': '???', '40b6': '???', '40b7': '???', '40b8': '???', '40b9': '???', '40ba': '???', '40bb': '???', '40bc': '???', '40bd': '???',

	'40be': '???', '40bf': '???', '40c0': '???', '40c1': '???', '40c2': '???', '40c3': '???', '40c4': '???', '40c5': '???', '40c6': '???', '40c7': '???',
	'40c8': '???', '40c9': '???', '40ca': '???', '40cb': '???', '40cc': '???', '40cd': '???', '40ce': '???', '40cf': '???', '40d0': '???', '40d1': '???',
	'40d2': '???', '40d3': '???', '40d4': '???', '40d5': '???', '40d6': '???', '40d7': '???', '40d8': '???', '40d9': '???', '40da': '???', '40db': '???',
	
	'40dc': '???', '40dd': '???', '40de': '???', '40df': '???', '40e0': '???', '40e1': '???', '40e2': '???', '40e3': '???', '40e4': '???', '40e5': '???',
	'40e6': '???', '40e7': '???', '40e8': '???', '40e9': '???', '40ea': '???', '40eb': '???', '40ec': '???', '40ed': '???', '40ee': '???', '40ef': '???',
	'40f0': '???', '40f1': '???', '40f2': '???', '40f3': '???', '40f4': '???', '40f5': '???', '40f6': '???', '40f7': '???', '40f8': '???', '40f9': '???',
	
	'40fa': '???', '40fb': '???', '40fc': '???', '40fd': '???', '40fe': '???', '40ff': '???', '4100': '???', '4101': '???', '4102': '???', '4103': '???',
	'4104': '???', '4105': '???', '4106': '???', '4107': '???', '4108': '???', '4109': '???', '410a': '???', '410b': '???', '410c': '???', '410d': '???',
	'410e': '???', '410f': '???', '4110': '???', '4111': '???', '4112': '???', '4113': '???', '4114': '???', '4115': '???', '4116': '???', '4117': '???',
	
	'4118': '???', '4119': '???', '411a': '???', '411b': '???', '411c': '???', '411d': '???', '411e': '???', '411f': '???', '4120': '???', '4121': '???',
	'4122': '???', '4123': '???', '4124': '???', '4125': '???', '4126': '???', '4127': '???', '4128': '???', '4129': '???', '412a': '???', '412b': '???',
	'412c': '???', '412d': '???', '412e': '???', '412f': '???', '4130': '???', '4131': '???', '4132': '???', '4133': '???', '4134': '???', '4135': '???',
	
	'4136': '???', '4137': '???', '4138': '???', '4139': '???', '413a': '???', '413b': '???', '413c': '???', '413d': '???', '413e': '???', '413f': '???',
	'4140': '???', '4141': '???', '4142': '???', '4143': '???', '4144': '???', '4145': '???', '4146': '???', '4147': '???', '4148': '???', '4149': '???',
	'414a': '???', '414b': '???', '414c': '???', '414d': '???', '414e': '???', '414f': '???', '4150': '???', '4151': '???', '4152': '???', '4153': '???',
	
	'4154': '???', '4155': '???', '4156': '???', '4157': '???', '4158': '???', '4159': '???', '415a': '???', '415b': '???', '415c': '???', '415d': '???',
	'415e': '???', '415f': '???', '4160': '???', '4161': '???', '4162': '???', '4163': '???', '4164': '???', '4165': '???', '4166': '???', '4167': '???',
	'4168': '???', '4169': '???', '416a': '???', '416b': '???', '416c': '???', '416d': '???', '416e': '???', '416f': '???', '4170': '???', '4171': '???',
	
	'4172': '???', '4173': '???', '4174': '???', '4175': '???', '4176': '???', '4177': '???', '4178': '???', '4179': '???', '417a': '???', '417b': '???',
	'417c': '???', '417d': '???', '417e': '???', '417f': '???', '4180': '???', '4181': '???', '4182': '???', '4183': '???', '4184': '???', '4185': '???',
	'4186': '???', '4187': '???', '4188': '???', '4189': '???', '418a': '???', '418b': '???', '418c': '???', '418d': '???', '418e': '???', '418f': '???',
	
	'4190': '???', '4191': '???', '4192': '???', '4193': '???', '4194': '???', '4195': '???', '4196': '???', '4197': '???', '4198': '???', '4199': '???',
	'419a': '???', '419b': '???', '419c': '???', '419d': '???', '419e': '???', '419f': '???', '41a0': '???', '41a1': '???', '41a2': '???', '41a3': '???',
	'41a4': '???', '41a5': '???', '41a6': '???', '41a7': '???', '41a8': '???', '41a9': '???', '41aa': '???', '41ab': '???', '41ac': '???', '41ad': '???',
	
	'41ae': '???', '41af': '???', '41b0': '???', '41b1': '???', '41b2': '???', '41b3': '???', '41b4': '???', '41b5': '???', '41b6': '???', '41b7': '???',
	'41b8': '???', '41b9': '???', '41ba': '???', '41bb': '???', '41bc': '???', '41bd': '???', '41be': '???', '41bf': '???', '41c0': '???', '41c1': '???',
	'41c2': '???', '41c3': '???', '41c4': '???', '41c5': '???', '41c6': '???', '41c7': '???', '41c8': '???', '41c9': '???', '41ca': '???', '41cb': '???',
	
	'41cc': '???', '41cd': '???', '41ce': '???', '41cf': '???', '41d0': '???', '41d1': '???', '41d2': '???', '41d3': '???', '41d4': '???', '41d5': '???',
	'41d6': '???', '41d7': '???', '41d8': '???', '41d9': '???', '41da': '???', '41db': '???', '41dc': '???', '41dd': '???', '41de': '???', '41df': '???',
	'41e0': '???', '41e1': '???', '41e2': '???', '41e3': '???', '41e4': '???', '41e5': '???', '41e6': '???', '41e7': '???', '41e8': '???', '41e9': '???',
	
	'41ea': '???', '41eb': '???', '41ec': '???', '41ed': '???', '41ee': '???', '41ef': '???', '41f0': '???', '41f1': '???', '41f2': '???', '41f3': '???',
	'41f4': '???'

	} 
	# Info on editing the images used to display these characters in-game can be found here: https://smashboards.com/threads/changing-menu-text.368452/page-2#post-21591476