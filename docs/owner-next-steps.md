# Owner handoff — what happens next

## Do not upload the prototype code into Wix

The files in `prototype/` are a visual and structural reference, not a Wix package. The classic Wix Editor cannot import this HTML/CSS as a native Wix page. Pasting it into an HTML embed would create an isolated frame, weaken editing, responsiveness, accessibility and SEO, and disconnect the design from Wix navigation, Bookings, Members Area and the existing site theme.

Do not paste the code into the Wix-connected ChatGPT conversation either. That connection is more useful for reading the current site, checking page/app dependencies and—only if it explicitly supports safe editing—working with native Wix elements. It does not need the prototype source to understand the approved direction.

## What the green Diff panel is—and is not

The green boxes in the Codex **Diff** panel show added source text. They are not a rendered website preview and are not an appropriate basis for visual approval. The owner is not expected to assess typography, spacing, colour balance or responsive design from that code view.

Do not answer the visual-review questions until a rendered desktop and mobile preview is available. The implementation team must provide either screenshots or a browser-accessible preview; asking the owner to infer the design from HTML/CSS is not an acceptable review handoff.

## What is needed from the owner now

### 1. Review the direction from a rendered preview

Once desktop and mobile visuals are supplied, review the homepage concept for these decisions:

- Does the opening feel like Stump’d?
- Is Next Ball prominent enough?
- Do Schools, Clubs, Players and Parents feel equally important?
- Does Spark → Foundation → Core make sense at homepage depth?
- Is the restrained Instagram section worth retaining?
- Does the final planning-call action feel appropriate?

The labelled logo and photography areas are placeholders only. Do not judge those as proposed graphics.

### 2. Supply existing assets as files

Provide:

- the official logo PNG as a downloadable file;
- three to six strong existing delivery photographs at original resolution; and
- one suitable photograph of Rob and Jack, if available.

If this task’s attachment control rejects the files, use one view-only cloud folder. Do not include customer data, Wix credentials or private account exports.

### 3. Wix dependency report — received

The owner supplied the read-only report. It confirms that the homepage has no Velo/dataset dependency, the header/footer are global, Captain’s Compass remains protected, Instagram uses the native connected feed, and the principal content pages can be consolidated without a code dependency. It also identified a homepage `noindex` directive and missing meta description.

### 4. Do not change the live site yet

After the direction and dependency report are reviewed, create a duplicate/unpublished homepage in Wix and rebuild the approved concept with native Wix elements. Keep the existing homepage published until desktop and mobile previews, links, Bookings and member functionality have been tested.

## Implementation choices

There are two safe routes:

### Route A — a Wix editor implements the concept

The owner or a Wix designer rebuilds the concept natively from the prototype and implementation notes, then shares Wix preview links/screenshots for review. This is the currently available route.

### Route B — direct assisted implementation

If a future project environment exposes the authenticated Wix tools/editor session, the implementation can be performed directly in an unpublished Wix copy. Access is only considered available when the tool can list the supplied site ID and its pages; a plugin-detail link or site ID alone is not edit access.

## Immediate next step

No visual feedback is due until the project supplies a rendered preview. The dependency report is complete.

The SEO and member-route approvals are complete: make the homepage indexable, use the approved metadata, remove the incorrect address without publishing the Bristol home address, and retain a quiet Captain’s Compass member-login route.

The project team—not the owner—now owns the next action:

1. turn the homepage wireframe into a rendered desktop and mobile visual concept using the approved palette;
2. place the real logo and existing photography when downloadable files are available;
3. present that visual in a format the owner can actually view, rather than as a source-code diff;
4. collect the six direction answers above;
5. revise the visual concept once; and
6. prepare a native Wix build sheet for an unpublished homepage copy.

Only after the rendered concept is approved should anyone reproduce it in Wix. The owner does not need to paste code, edit the current site or request another dependency report.

Assets can follow when convenient. No code should be pasted into Wix at this stage.

## How Codex work progresses

Codex does not continue working in the background after it sends a response, and it cannot later initiate a message to announce that work is ready. Work advances when the owner sends the next instruction in this task.

No technical setup is required from the owner. To start the next stage, send:

> Please proceed now with the rendered desktop and mobile homepage concept. Use placeholders where the downloadable logo or photographs are not yet available, and do not change the live Wix site.

That message authorises the next active work turn. Codex should then complete as much of the visual deliverable as the environment supports, clearly identify any genuine limitation, and return something viewable. The owner should not be asked to infer a design from source code or wait for an unobservable background process.
