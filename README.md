# TCC_Cand_Netchange_Parser
Parses the results file for a Taleo Connect Client Candidate Netchange

This is a python script that parses the key result fields from a TCC Candidate Netchange results file by searching for the result 
identifier text and parsing the corresponding counts. It also extracts all error messages from the result contents. This has been 
scripted to accomodate a 'scrubber' process, which removes SSOIDs and other employment data upon loss of Internal status.

Note - I locally compiled as an executable using pyinstaller.

UPDATE - appearently you can achieve similar if not better results using the TCC Custom Steps library
Additional update - I have successfully used the custom step: com.taleo.integration.client.customstep.mail.SendEmailPostStep to alert us on row-level errors for an import. This is great, but one thing this parser does is allow you to recursively parse a number of output files and perform trend analisys (i.e. increase in volume / errors).
