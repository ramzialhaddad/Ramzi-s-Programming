/* __              __ 
  / /_____  ____  / /_  toot.h v1.0.6 [Dec 5, 2017] zlib licence
 / __/ __ \/ __ \/ __/  cross-platform library and command line tool to toot "tooooot"
/ /_/ /_/ / /_/ / /_    file created [November 7, 2017]
\__/\____/\____/\__/    Copyright (c) 2017 Guillaume Vareille http://ysengrin.com
 a beep that beeps       ____________________________________
                        |                                    |
                        |    email: toot at ysengrin.com     |
                        |____________________________________|
- License -

This software is provided 'as-is', without any express or implied
warranty.  In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
claim that you wrote the original software.  If you use this software
in a product, an acknowledgment in the product documentation would be
appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
*/

#ifdef __cplusplus
extern "C" {
#endif
	
extern char toot_version[8] ; /* contains tinyfd current version number */

extern int toot_verbose ; /* 0 (default) or 1 : prints the command line calls */

void toot(float aFrequency_Hz, int aLength_ms) ;

#ifdef __cplusplus
}
#endif
