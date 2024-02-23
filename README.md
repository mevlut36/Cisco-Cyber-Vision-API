# Cisco Cyber Vision

Cyber Vision is a Cisco supervision tool that enables in-depth analysis of the various devices (IT/OT) in a network infrastructure.

It enables :
- analysis of device vulnerabilities
- Search for devices on the network by IP address, model or name
- Incident and event management

Despite all this, Cyber Vision's Web interface doesn't allow it to be used to its full potential.

What pushed me into this project was that I needed to retrieve and filter all the OT machines on a network, and I came across several problems:
- I wanted to add each machine to a group, but group creation is twisted on C-V. (Choose a machine then create the group from the machine)
- Adding machines to a group is too long and tedious, you have to manually add each machine (The add machine to group button is not obvious).

  That's why I decided to launch this project using the C-V API.
  The functionality I'm working on at the moment is to add a selection of machines via a .csv file to a group.
  The time saved is considerable!