# Sending Commands to a PHP Webshell

## General Information

- Author: Ryan Hoy
- Date: 12/8/2018
- Description: This presentation covers a few different ways to interact with a PHP backdoor webshell in order to demonstrate understanding a specific aspect of the HTTP protocol and how to automate interaction with it. This page and associated presentation are for the Cyber Operations I (CSC840) course at [Dakota State University][dsu].
- Video Presentation: [Available on YouTube][yt]

## Why You Should Care

Understanding network protocols, such as HTTP, can help information security professionals operate with a higher level of competence. From a defensive standpoint, understanding the types of network traffic that is expected on the network can help the web and firewall administrators determine appropriate configurations. From the offensive viewpoint, an intimate understanding of how a protocol like HTTP works, and how it can be manipulated, might expose vulnerabilities that would have been otherwise unaddressed.

Given the often manual process associated with protocol analysis, it becomes important to be able to automate processes once the function is understood. The Python scripting language, among others, is well suited to prototype tools that will interact with network protocols like HTTP.

In this example, a php web shell is used to demonstrate how an attacker could use their knowledge of passing parameters to the shell in a GET request in order to gain code execution on a compromised web server. 

## Three Main Ideas

1. It is possible to examine the contents of HTTP traffic using a proxy like Burpsuite. Other protocols could be examined with a tool like Wireshark or `tcpdump`.
2. Once you understand the contents of network traffic, HTTP in this case, it can be modified with Burp Repeater to achieve different results.
3. Scripting, using a language like Python, can enable an analyst or attacker to quickly prototype a solution to interact with protocols.

## Future Direction

This topic could be further explored by expanding the robustness of the script used to automate interaction with the web shell. Additionally, a backdoor written in Python could be written to provide more advanced functionality beyond simple command parsing. 

## Additional Resources

- [BurpSuite Homepage][burp]
- [DVWA Homepage][dvwah]
- [DVWA Repo][dvwar]
- [Lesson][lesson] on how to upload a PHP backdoor to DVWA


[dsu]: https://dsu.edu/graduate-students/phdco
[burp]: https://portswigger.net/burp/
[dvwah]: http://www.dvwa.co.uk/
[dvwar]: https://github.com/ethicalhack3r/DVWA
[lesson]: http://www.computersecuritystudent.com/SECURITY_TOOLS/DVWA/DVWAv107/lesson8/
[yt]: https://youtu.be/ba_3qU7K43k
