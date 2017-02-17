# Archlinux.org's scrapper

Acordding to the
[ArchWiki](https://wiki.archlinux.org/index.php/System_maintenance#Read_before_upgrading_the_system):

> Read before upgrading the system
> 
> Before upgrading Arch, always read the latest Arch News to find out if there are
> any major software or configuration changes with the latest packages. Before
> upgrading fundamental software (such as the kernel, xorg, systemd, or glibc) to
> a new version, look over the appropriate forum to see if there have been any
> reported problems. 

And they are right, one should be at least following the latest news before
upgrading.

### Heads up!

`lsrdg/archlinux-scrapUP` is damn small script, wrote by an un-developer and it
has such a tiny functionality that it shouldn't deserve your attention. It was
written for personal use _only_. 

If you are *serious* about checking everything before the system upgrade, you
probably want to check these links out:

- [Pacmatic](http://kmkeen.com/pacmatic/) > Get emails about pending system
  updates with cron-pacmatic
- [Pacman/Tips and tricks -
  utilities](https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks#Utilities)
  > wiki.archlinux.org page with real tips.

## scrapUP

Archlinux-scrapUP will just show you the title of the latest new from
archlinux.org before calling for `$ sudo pacman -Syu`. If the news's header is
kind of new for you, you should probably avoid upgrading. In instead, go find
out if you should something.

PS: I'm no ArchExpert. The words above are there only for remind me that - damn!
- I should have read that before!

## Requirements

- Archlinux (yay o/)
- [Python 3*](https://wiki.archlinux.org/index.php/Python#Python_3) with the
  _requests_, _bs4_ and _lxml_ modules.

## Installing

Clone this repository and add the following to your `.bash.rc`:

```
# scrap archlinux.org before full upgrade
alias scrapUP='python ~/PATH-TO/archlinux-scrapUP/scrapUP.py ; sudo pacman -Syu'
```


A few things should also be noted:
- Be sure to change `/PATH-TO/` to the real path to the cloned repository.
- the alias above (on the `.bashrc`) assumes that `python` calls *python3*.
- if you really read 'till here your arch\*/develp\*/prog\* kungfu's skill might
  be worse than mine and in this case, you shouldn't be trying to use it.


## Usage

Just run `$ scrapUP` and it will print the title of the latest new and call `$
sudo pacman -Syu`. As of today (ho, well) it looks like this:

```
$ scrapUP 

Phasing out i686 support

[sudo] password for YOUR_USERNAME: 
```
