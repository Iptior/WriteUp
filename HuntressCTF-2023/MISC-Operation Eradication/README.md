# MISCELLANEOUS - Operation Eradication

## Description

<img align="center" src="screen/01-Description.png" alt="Description of the challenge" />

We have 1 file and 1 site.

## WebSite

When I saw the website, I understood that I must to delete the data :

<img align="center" src="screen/02-WebSite.PNG" alt="Description of the challenge : website" />

So, let’s take a look at the challenge file's.

<img align="center" src="screen/03-conf_file.PNG" alt="The conf file of the challenge" />

It's a rclone configuration!

With a script, I decrypt the password : *SuperExtremelySecurePasswordLikeAlways*

<img align="center" src="screen/04-decrypt_password.PNG" alt="Decrypt the password" />

I can use this configuration to copy the data on my computer.

<img align="center" src="screen/05-Copy_and_Tree.PNG" alt="Copy the depot and tree" />
<img align="center" src="screen/06-Tree.PNG" alt="End of the tree command" />

Ok, i have the 133 files!

Let's go, i will purge the depot...

<img align="center" src="screen/07-rclone_purge.PNG" alt="Purge" />

I don't have the permission...

Maybe i can sync from my PC to the remote repository ! I remove 1 file and sync.

<img align="center" src="screen/08-rm_file_and_sync.PNG" alt="Remove one file and sync" />

I can not delete a file, so recreate but empty !

<img align="center" src="screen/09-Good.PNG" alt="It's good" />

It's work !

## The Flag 

I do the same technique for the rest of the files and ...

<img align="center" src="screen/10-flag.PNG" alt="The flag" />
