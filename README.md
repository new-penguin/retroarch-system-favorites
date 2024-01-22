# Retroarch System Favorites

This script will move (not copy unless you modify the script) your Retroarch favorites to the relevant system playlist and append a * so they're first to show. Retroarch doesn't support special characters like ⭐ so we'll have to make do with appending an asterisk for now. Maybe we can cope without those fabulous stars. 

<b>Usage</b>:   
Place into your retroarch folder, ie, ~/.config/retroarch. You can set this to run on OS boot or run just before Retroarch executes like so if started via terminal or editing a start menu entry...

```./retroarch-system-favorites.bin & retroarch```  

Two scripts are provided, one to keep the old game entry in the playlist after appending as a favorite (retroarch-system-favorites-append) and one to replace the old game entry and append as a favorite (retroarch-system-favorites-replace), if you'd like to reduce redundancy in the playlist. The only drawback of the latter is once you favorite a game, you have to unfavorite by renaming it whereas with it appended, you can just delete the favorite entry using Retroarch and not worry about deleting the only game entry in the system playlist. [^1]
    
    
  ![retroarch-system-favorites](https://github.com/new-penguin/retroarch-system-favorites/assets/139792946/a42c8da8-1a33-42c0-9ac1-3a0af1931ebd)

[^1]: I tested this on my own system and it's still the same lovely machine that it's always been. But please backup your playlist files as this will overwrite relevant playlists associated with your favorites.
