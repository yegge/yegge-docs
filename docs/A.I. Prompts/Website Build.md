# Website Build
---
-------------- star copy below this line-------------
## Website Prompt and Proposal (NO SERVICES)
###### PURPOSE:  To develop a relational database driven static website at a minimal hit to the wallet.  Budget is important, but not at the expense of quality.  It should be a website operation that can exist with minimal to no maintenance or interaction other than updating with new content.  In other words it should carry on after I pass away.

###### I’m a musician and I’m in need of a website to catalog my work.  I have two music projects I’d like to represent.  The two projects go by the pseudonyms that they are published under as the album artist.  Those pseudonyms are “Angershade” & “The Corruptive” the publishing company/record label name under both projects is called “Yegge”.  The domains I have with this website are yegge.com, angershade.com, & thecorruptive.com.

###### Design with a Glassmorphism style using frosted glass effects with transparency and backdrop blur. Elements should have subtle light borders (1px) and slight transparency. Create depth through layering of translucent elements. Use colorful backgrounds (gradients work well) with frosted glass UI elements on top. Apply backdrop-blur CSS properties and use RGBA colors with alpha transparency. Aim for a modern, clean aesthetic with subtle light reflections and shadows. The design should be unique, beautiful and detailed. the colors should reflect a dark mode style and feel.  Font- family system font or Inter for headings and paragraphs.

FOLDER HIERARCHY
	WEBSITES
	adminpanel/
           index.html (all the ways to administer and update the sights)
		assets/
			css/ (design elements consistent across all sites)
			js/(consistent scripting for all sights)
			img/ (images)
			audio/ (.mp4 for streaming)
		Yegge/
			index.html
		Angershade/
			index.html (blog filtered)
			discography (discography filtered)
		The Corruptive/
			index.html (blog filtered)
			discography (discography filtered)
		blog/
		discography/
         subscribe/ (from to subscribe to newsletter)
		 inquiry/ (form to get in contact)

Footer: (there should be away to add to this per site in admin-panel)
© 2025 <a href=“https://hyperfollow.com/brianyegge”>Brian Yegge</a> | <a href=“https://hyperfollow.com/angershade”>Angershade LLC</a> | <a href=“https://hyperfollow.com/thecorruptive”>The Corruptive</a> | ℗ Yegge

I.  BLOG: 

I would like to have a blog that can be sorted by category, the categories would be “Angershade” “The Corruptive” & “Yegge” which I will set via each post.  It should have a way to tag posts as well.   Blog editor should have a way to blog in rich text, html, markdown, picture gallery uploads, and code blocks with all code able to be rendered when published.  There should be an ability to create drafts as well, and post date blog posts and schedule future blog posts.

II. DISCOGRAPHY 
DATABASE to be created for the purpose of display of my catalog.  It will also serve as an organizational tool on the back end to help define progress and show where progress needs to be made, this is measured by the track as defined in the logic below. An admin panel and view is required with an easy to use interface to update the storage and the databases. The domain is yegge.com, the admin site could be yegge.com/admin, the files will be accessible across a total of three domains, yegge.com. angershade.com, thecorruptive.com. 
 THE DATA 
This will be a relational database of music and metadata.  There will be one catalog each in two parts.  The DISCOGRAPHY/database will consist of both published music and works in progress with PUBLIC VIEW restrictions, a VIP view with restrictions, and an admin view with NO Restrictions, along with an admin panel for entering the data.  The PUBLIC VIEW will have subviews that are determined by the Album Artist field, example, Angershade.com will only show the albums listed under the ALBUM ARTIST “Angershade” same for thecorruptive.com to show “The Corruptive”. The two tables (parts) are ALBUM TABLE & TRACKS TABLE, the tracks will be related to the ALBUM ID (PARENT) that they were published on. It will consist of the following data to be displayed or hidden on the website.  

SCHEMA
ALBUM TABLE:
		ID: INTEGER | PRIMARY KEY
		ARTWORK GALLERY: (linked by URL thumbnails for each of the following (Front Cover) (BackCover) (Sleeve) (Sticker) Front cover 		displayed on a carusel and contained by default.  			Clicking on any of thumbnail will pop large within the page like a gallery.  Images to be 		hosted via a bucket on Cloudflare’s R2 Object Storage.)
		ALBUM NAME: VARCHAR(255) (allowed to be URL linked)
		ALBUM TYPE: ENUM | e.g. EP, LP, SP, Compilation
		ALBUM ARTIST: VARCHAR(255) (allowed to be URL linked)
		CATALOG NO.: VARCHAR(255) Format will be ANG-## for Angershade Releases, COR-## for The Corruptive Releases, YEG-## for Yegge Releases, (## to be entered as 01, 02, 03, 			etc. but when rendered on a website it should display as a roman numeral equal to the integer entered)
		ALBUM DURATION: (To be determined by adding together the INTEGERS in the TRACKS DURATION Field.   Format ##:## First set of ## minutes : Second set seconds.)
		UPC: VARCHAR (20) (ADMIN/VIP VIEW only)
		DISTRIBUTOR: TEXT LINKED (allowed to be URL linked)
		LABEL: TEXT LINKED (allowed to be URL linked)
		RELEASE DATE: DATE  		REMOVAL DATE: DATE
		VINYL & CD RELEASE DATE: DATE
		PRODUCER: TEXT (allow to be URL linked) (BUTTON: Allow to add more than one)
		ENGINEER: TEXT ( (allow to be URL linked) ) (BUTTON: Allow to add more than one)
		MASTERING: TEXT (allow to be URL linked) ) (BUTTON: Allow to add more than one)
		KEY CONTRIBUTORS: TEXT (NAME & CONTRIBUTION) (allow to be URL linked) ) (BUTTON: Allow to add more than one)
		ALBUM STATUS: (Select One: In Development, Released, Removed)
		VISIBILITY: dropdown menu
		PUBLIC: Viewed on website
		ADMIN: Viewable to the admin only, hidden from public view. 		VIP: Generate a random link to view
		STREAMING LINKS: URL (Apple Music, Spotify, Youtube Music, iTunes, Amazon Music, Tidal, Bandcamp,) 		PURCHASE: URL (CD, VINYL, DIGITAL DOWNLOAD) 		ALBUM COMMENTARY: TEXT BOX 	


TRACK TABLE: 
	TRACK ID: Integer | Primary Key
	ALBUM ID: Integer | Foreign Key
	TRACK NO.: INTEGER | For sorting on Album 
	TRACK NAME: TEXT 	ALBUM NAME: VARCHAR(255) 	DURATION: INTEGER | to contribute to the album duration.  Format ##:## First set of ## minutes : Second set seconds
	ARTIST NAME: TEXT (allow to be URL linked) ) (BUTTON: Allow to add more than one)
	COMPOSER(S): TEXT (allow to be URL linked) ) (BUTTON: Allow to add more than one)
	KEY CONTRIBUTORS: TEXT (Optional: LINK TEXT TO URL) (BUTTON: Allow to add more than one)
	ISRC: VARCHAR(15) (ADMIN/VIP VIEW ONLY) 
	TRACK STATUS: SELECTION (WIP, B-SIDE, RELEASED, SHELVED) 	STAGE OF PRODUCTION: SELECTION (CONCEPTION, DEMO, IN SESSION, OUT SESSION, In MIX, Out MIX, IN MASTERING, Out 			MASTERING, SHELVED, REMOVED, RELEASED)  	STAGE OF PRODUCTION DATE: (SET TO TODAY’s DATE*)
		if TRACK Status is set to release, STAGE is automatically set to released and date updated to the PARENT ALBUM RELEASE 		DATE otherwise STAGE OF PRODUCTION DATE defaults to the last date updated)  
	VISIBILITY: Inherit from ALBUM Visibility
	Track Duration: INTEGER | MM:SS
	STREAM: EMBEDDED CONTENT (with checkbox on the admin side to prevent streaming and provide an slightly dark overlay over 	the wave file) 	PURCHASE DIGITAL DOWNLOAD: (URL to purchase download)
	TRACK COMMENTARY: TEXT BOX

III.  SUBSCRIPTION PAGE:
 	A form with the following fields.
		FIRST NAME: TEXT (REQUIRED) 		LAST NAME: TEXT (REQUIRED) 		PHONE NUMBER: phone number field (OPTIONAL) 		EMAIL ADDRESS: email (REQUIRED)
		COUNTRY: Dropdown with list of countries (REQUIRED)
		SUBMIT BUTTON
	Upon submission, Redirect to a thank you page confirming submission.
		Append to a subscription database

IV.  INQUIRY/CONTACT PAGE:  
	A form same as contact without the subscribe	
		FIRST NAME: TEXT 		LAST NAME: TEXT 		PHONE NUMBER: phone number field 		EMAIL ADDRESS: email 		PREFERRED MESSENGER: Option to pick the following: (iMessage, SMS, Facebook Messenger, WhatsApp) 		MESSAGE: TEXT BOX 		SUBMIT BUTTON
Upon submission, Redirect to a thank you page confirming submission.
		Send to email admin@yegge.com with prefilled subject “WEBSITE INQUIRY”

V.  TERMS OF SERVICE PAGE (Markdown format)

# TERMS OF SERVICE/USE
###### Updated August 2, 2025


 ###### By using Angershade.com, Yegge.com, thecorruptive.com, & services by Yegge, you agree to these Terms. 
 Disagreement means refraining from using content and/or services.

### Music Sales

Media from Angershade.com, Yegge.com, thecorruptive.com, is for personal use. Commercial use requires explicit permission. Downloads come with a personal use license and are non-refundable, including for various file formats. Personal use allows storage and backup but forbids sharing, redistribution, or resale. The seller retains all copyrights and is not responsible for file compatibility or quality. Violating these terms leads to indemnification responsibilities. Purchasing and downloading signifies agreement to these terms. Additional licensing options are available.

### Terms for Free/Paid Downloads

These terms apply to music from Angershade.com. Downloading signifies agreement.

Copyright: Music is © *Angershade/Brian Yegge, unless otherwise specified.
Personal Use: For private, non-commercial enjoyment.
Commercial Use: Requires permission or a license.
Redistribution: Forbidden.
Attribution: Credit Angershade and provide a website link.
Disclaimer: Music is "as is" without warranties.
Liability: The artist is not liable for any damages.
Changes: Terms may change, and updates will be posted.
Contact: For licensing or inquiries, fill out the form.
All Downloads come with a PDF copy of the Personal Use agreement.

Commercial Use is specifically tailored to the intended nature & desired use.

### Photography Services

Models must be 18+ (Women Only) - if you find this to be discriminatory and/or Sexist, I don’t care.
Book and confirm appointments in advance.
Refer to individual agreements for cancellations and refunds.
Social media/website use requires a single-use license.
Copyright: Photographs are © Yegge/Brian Yegge, unless otherwise specified.
Personal Use: Viewing and sharing for non-commercial purposes.
Commercial Use: Requires permission or a license.
Attribution: Credit Brian Yegge and provide a website link.
Alterations: Prohibited without explicit permission.
Disclaimer: Photographs are "as is" without warranties.
Liability: The photographer is not liable for any damages.
Changes: Terms may change, and updates will be posted.
Contact: For licensing or inquiries, contact here.
Privacy Policy (Last updated: August 21, 2023)

### Angershade.com, Yegge.com, thecorruptive.com, respects your privacy.

We collect personal (name, email, etc.) and non-personal (IP address, browser type, etc.) information.
We use this information for website maintenance, user inquiries, and, if agreed, for newsletters and promotions.
We don't sell your information. Disclosure occurs with consent, for policy enforcement, or legal reasons.
External links and third-party services have their own privacy policies.
We protect your data but can't guarantee absolute security.
We don't knowingly collect children's information (under 13).
The Privacy Policy may change, and we'll update the "Last updated" date.
Contact us for any privacy concerns.
Limitation of Liability

Angershade.com, Yegge.com, thecorruptive.com, isn't liable for indirect damages from using the website or services. Terms can change without individual notice. Stay updated with the website for the latest terms.

### Fair Use

Respect the intellectual property of image creators. Share for educational or non-commercial purposes with proper credit. For commentary, criticism, or reporting, ensure fair representation. Seek permission for uncertain uses. Report violations and comply with this policy for a respectful sharing environment.

###### *In case of the owner's demise, ownership rights transfer to the next of kin.

###### **All Downloads come with a PDF copy of the Personal Use agreement.

###### ***Commercial Use is specifically tailored to the intended, desired use.

###### ****Photographer Owns All Images as it defaults to law.  Unless otherwise specified.

###### Angershade.com, Yegge.com, thecorruptive.com,


——— 

USING a MacBook Pro M3 Pro with 36GB of unified memory & a Mac mini M2 PRO 32GB of unified memory