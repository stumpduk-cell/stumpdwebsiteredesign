# Stump’d Schools page — Phase 3 implementation pack

## Status

The Phase 1 direction was approved by the owner on 13 September 2026. This pack turns that direction into a Wix-ready page structure, copy deck and responsive build specification. It does not invent Foundation/Core delivery formats or edit the live Wix site without collaborator access.

The supplied editor screenshot confirms that the site uses the classic **Wix Editor**, not Wix Studio: the editor URL contains `/html/editor/`, and the toolbar exposes separate desktop and mobile views rather than Studio breakpoints. Tablet behaviour must therefore be verified through browser-width testing of the published/preview page rather than treated as an independently designed Studio breakpoint.

### Design latitude clarified

The owner has confirmed that the existing website’s layout and styling are not constraints. The logo is fully locked, and the logo colours plus approved supporting colours from the Stump’d app form the locked colour system. The next visual exploration may therefore start from a clean page architecture rather than reproducing the current Wix composition.

This is permission to redesign, not to discard the brand. The recommended approach is a **brand-led reset**:

- preserve the official logo exactly;
- preserve the approved colour system;
- preserve programme names, facts, Stump’d language and the confident human tone;
- retain existing visual devices only when they improve recognition, clarity or energy;
- reconsider typography, grids, texture, navigation and section composition as a coherent new system; and
- use authentic Stump’d photography rather than replacing it with stock or generated people.

The current static prototype should now be treated as a content-flow wireframe, not the preferred final art direction. The redesign will begin with the homepage so that navigation and the site-wide visual system are resolved before Schools is rebuilt. The later Schools concept should demonstrate the hero, pathway and Spark section on both desktop and mobile. Typography should be changed only when the alternative is shown alongside the existing American Typewriter/Roboto pairing and provides a clear readability or hierarchy benefit.

## Confirmed decisions

- The supplied PNG is the official logo master currently available.
- Delivery photographs were taken by the owner and have the necessary permissions.
- Spark serves Years 5–6 / ages 9–11.
- Foundation serves ages 11–13.
- Core serves ages 14–17.
- 1-to-1 mentoring remains active and secondary to the three-stage pathway.
- Summer Series has ended and should be removed from navigation.
- “Book a planning call” is the primary contact route.
- No extra safeguarding or privacy statement is required specifically for the supplied delivery photography.
- There are no Spark-specific photographs currently available. Use a suitable authentic Stump’d delivery image without labelling it as Spark-specific.
- Log In leads to a member area, but there are no active members. Remove it from the primary header; do not delete the underlying member area in this phase.
- The existing page aesthetic is not locked. Only the official logo, its brand colours, approved app supporting colours and established Stump’d content/language constrain the new visual exploration.

## Wix access required

### Preferred access route

The most useful access is an authenticated Wix editor session made available through the project’s browser/session-sharing integration. That lets the implementer inspect the exact editor type, duplicate the Schools page, work on an unpublished copy, test responsive layouts and return a preview without exchanging account credentials.

If the collaboration platform provides an email address for the implementer, invite that address through Wix as a collaborator. Start with the least-privilege role that can edit the website, menus and media library. Add publishing permission only if direct publication is explicitly required. **Never paste the owner’s Wix password, recovery code, payment details or a long-lived session cookie into chat.**

This repository workspace does not itself provide an email inbox, interactive browser hand-off or persistent Wix login. A collaborator invitation sent without one of those mechanisms cannot be accepted here. Full account-owner access would therefore add risk without enabling the work; scoped editor access is preferable.

To implement directly in Wix, invite the implementer as a site collaborator with permission to:

1. edit the site and its desktop/mobile layouts;
2. manage the site’s media library;
3. edit menus and the global header/footer;
4. view—but not manage payments for—the existing planning-call service sufficiently to test its link and booking journey; and
5. publish only if the owner wants direct publication. Otherwise, retain publishing rights and review the staged version first.

The least-privilege choice is the Wix role that permits website editing and media/menu management without billing, domain or payment permissions. The role name can vary with Wix setup and editor generation, so verify its listed permissions rather than relying only on its label.

If authenticated access cannot be made available, the best fallback package is:

1. the Wix editor type in use (Wix Editor or Wix Studio);
2. a screen recording moving from the dashboard into the Schools page editor and its mobile view;
3. screenshots of the Pages & Menu panel, site styles, layers for the Schools page and mobile layout;
4. the original logo and selected Spark photographs as downloadable files rather than compressed screenshots;
5. a Wix preview link after each implementation pass; and
6. confirmation of whether Log In supports an active member area before it is removed or demoted.

For the new visual concept, also supply the app’s supporting-colour values or an export/screenshot of its design tokens. Do not sample approximate colours from compressed screenshots when exact values are available.

To identify the editor type when the dashboard does not label it, open **Edit Site** and inspect the editor URL and interface. Capture the full address bar and editor toolbar in a screenshot; that is enough to distinguish the editor without sharing credentials.

If a screen recording will not upload to the collaboration task, export or convert it to an MP4 using H.264 video and AAC audio, reduce the resolution to 1080p, and try a shorter recording. The current `.webm` recording may be rejected because of file type, codec or upload-size limits. If MP4 also fails, split the recording into two or three shorter files, upload key screenshots instead, or provide a view-only cloud-storage link with link access enabled and no edit permission. Do not use a public link if the recording exposes private customer, booking or account information.

Before editing, duplicate the current Schools page as an unpublished backup and record its current SEO title, description, slug and booking URL. Keep `/stump-d` unless there is a separately approved redirect plan.

## Global header changes

- Remove Summer Series.
- Keep the official logo linked to Home.
- Make Schools easy to identify in the primary navigation.
- Move social links to the footer rather than presenting them as the first task in the Schools journey.
- Remove Log In from the primary header because the member area has no active members. Keep the underlying member-area feature intact so this navigation decision remains reversible.
- Do not place a large planning-call button in the header on this first iteration. The page earns that action through its content and closes with it.

## Page structure and copy deck

Copy below is implementation-ready where marked **approved fact**. Foundation/Core summaries are deliberately conservative until their delivery formats are supplied.

### 1. Hero — what Stump’d is

**Eyebrow**  
STUMP’D IN SCHOOLS

**H1**  
Think well.  
Play better.

> In the rendered heading, preserve the official strapline capitalisation as **Think Well. Play Better.** The line break is visual only.

**Lead**  
Mental strength through cricket—for sport, school and everyday life.

**Supporting copy**  
Cricket is the training ground. Confidence, focus and resilience are the skills they take with them.

**Optional text link, not a filled primary button**  
Explore the school pathway ↓

**Image direction**  
Use one authentic, active delivery image with a subject positioned to leave clear negative space for the headline. Do not overlay body copy on a visually busy area.

### 2. Why it matters — better thinkers

**H2**  
Develop better players by developing better thinkers.

**Body**  
Pressure does not only arrive in a match. It shows up after a mistake, in the classroom, within a team and when confidence drops.

Stump’d gives young people simple ways to recognise what is happening, reset and choose what they do next.

**The Stump’d 5**  
Think. Reset. Focus. Communicate. Lead.

**Closing line**  
Cricket has always trained hands. Stump’d trains minds.

**Editorial note**  
Do not add a second generic benefits list here. The Stump’d 5 provides the scannable structure.

### 3. The Stump’d Pathway

**H2**  
The Stump’d Pathway.

**Intro**  
A clear progression in age, understanding and pressure.

#### Card 1 — Spark

**SPARK**  
Years 5–6 | Ages 9–11  
Confidence • Emotions • Teamwork

Building confidence before pressure increases.

- Recognise how emotions affect what happens next
- Use simple tools to reset and refocus
- Respond to mistakes with confidence

**Think. Reset. Next Ball.**

#### Card 2 — Foundation

**FOUNDATION**  
Ages 11–13  
Confidence • Emotions • Resilience

An introduction to mental strength through sport.

- Recognise how pressure and emotions show up
- Understand that nerves are normal
- Use simple tools to reset, refocus and support teammates

**Editorial constraint**  
This lightly edits the existing summary for consistency. Do not add a delivery duration until confirmed.

#### Card 3 — Core

**CORE**  
Ages 14–17  
Pressure • Performance • Responsibility

For teenagers navigating real pressure.

- Build awareness of pressure and setbacks
- Strengthen self-talk and focus
- Take responsibility for how responses affect teammates

**On the pitch. In school. In life.**

**Editorial constraint**  
Do not use “flagship” unless that hierarchy remains commercially intentional. Do not add a delivery duration until confirmed.

#### Secondary strip — 1-to-1 mentoring

**OPTIONAL 1-TO-1 MENTORING | AGES 13+**

Individual support for students who want to take the Stump’d tools further.

Keep this visually subordinate to the three cards. Retain detailed current mentoring copy only after checking it remains accurate.

### 4. Spark — dedicated editorial section

**H2**  
Spark.

**Subheading**  
Mental strength starts before the pressure does.

**Body**  
Spark is for Years 5 and 6. Across two practical sessions, children learn to recognise emotions, respond to setbacks and focus on what comes next.

They practise confidence, communication, teamwork and personal responsibility through activities they can understand and use.

**Next Ball statement**  
You can’t change what just happened.  
You can choose what you do next.

**Delivery facts**

- Years 5 & 6 | Ages 9–11
- Maximum 12 pupils per group
- Two 2-hour sessions per group
- The second session takes place one week after the first
- As many groups as your school requires

**Closing line**  
Step back. Take a breath. **NEXT BALL.**

**Accuracy note**  
Never describe Spark as a six-week programme for each child. A wider delivery period may contain several groups, but each group receives two sessions one week apart.

**Image direction**  
Choose the closest suitable authentic Stump’d delivery photograph showing children participating, thinking or communicating. No Spark-specific photographs are currently available, so do not caption or describe the selected image as a Spark session. Prefer an existing authentic image over stock or generated photography.

### 5. Already in schools — proof, not promotion

**H2**  
Already in schools.

**Body**  
Spark has been delivered for Gloucester Rugby Foundation using BBC Children in Need funding, reaching more than 50 children across multiple schools in the GL postcode during the term.

Each group received two sessions, one week apart. The wider delivery period covered multiple groups—it was not a six-week commitment for each child.

**Pull line**  
More importantly, Next Ball stuck.

**Body**  
Children and teachers began using the phrase themselves beyond the immediate exercises. That matters because the idea is simple enough to remember and useful beyond cricket.

**Accuracy note**  
Do not say “in partnership with BBC Children in Need”. Do not format the observed adoption as a quotation or testimonial.

### 6. How it works in your school

**H2**  
Built around your school day.

**Intro**  
No specialist cricket facilities are needed.

**Practical list**

- Stump’d brings the equipment
- Your school provides a classroom, hall or suitable outdoor area
- School staff remain present during delivery
- Sessions can be planned around your timetable
- Spark can scale to as many groups as your school requires

**Closing line**  
Clear structure. Practical delivery. Tools young people can use.

### 7. Final action

**H2**  
Start with a conversation.

**Body**  
Tell us about your pupils, timetable and what you want the programme to support. We’ll help you identify the right place to begin.

**Primary button**  
Book a planning call

**Destination**  
`https://www.stumpd.co.uk/booking-calendar/planning-call?referral=service_list_widget`

Do not add a competing filled button. A small plain-text email/contact link may be added later only if evidence shows visitors need an alternative.

## Visual system

### Colour roles

- `#10141e` — page and campaign background
- `#cf7f20` — editorial headings, primary rules and primary CTA
- `#a21340` — restrained emphasis, pathway connector accents and selected Next Ball details
- `#decdaf` — body copy and secondary headings

Do not add green as a dominant colour. Do not use unstyled blue emoji ticks.

### Typography

- American Typewriter: H1–H3 and short editorial pull lines.
- Roboto: body copy, labels, lists, buttons and functional content.
- Do not use American Typewriter for dense pathway bullet copy.
- Keep body lines near 55–70 characters on desktop.
- Use responsive heading sizing; visual scale should not force words outside the viewport.

### Suggested responsive ranges

These are starting points, not fixed values. Confirm them in the actual Wix editor and on devices.

| Element | Desktop | Tablet | Mobile |
| --- | ---: | ---: | ---: |
| H1 | 72–96 px | 56–72 px | 42–54 px |
| H2 editorial | 56–76 px | 46–60 px | 36–46 px |
| H3/card title | 26–34 px | 24–30 px | 26–30 px |
| Body | 18–20 px | 17–19 px | 17–18 px |
| Small labels | 14–16 px | 14–16 px | 14–16 px |

Use body line height around 1.5–1.65. Do not reduce copy below 16 px to make a card fit.

### Spacing

- Use a consistent section rhythm rather than individually positioned empty space.
- Desktop section padding: approximately 112–144 px vertically.
- Tablet section padding: approximately 80–104 px vertically.
- Mobile section padding: approximately 56–72 px vertically.
- Keep content within a shared maximum-width container; allow photographs and selected campaign textures to break out deliberately.

### Pathway construction

- Build cards from Wix containers, text and lists—not one flattened image.
- Desktop: three equal cards in one row, joined by a horizontal progression line.
- Tablet: three readable columns where possible; otherwise use an intentional two-plus-one layout.
- Mobile: Spark, Foundation and Core stacked vertically with a vertical connector.
- Preserve the existing black texture, gold borders and subtle magenta details.
- Hide decorative texture from assistive technology and keep every essential label as live text.

### Image treatment

- Use owner-supplied Stump’d photography only.
- Set focal points independently for desktop and mobile.
- Prefer movement, concentration and interaction over empty facilities.
- Use restrained contrast/grade adjustments consistently; do not apply filters that obscure faces.
- Add useful alternative text describing the activity, not marketing copy.

## Responsive acceptance criteria

### Desktop

- The proposition and school audience are understandable without scrolling through the entire hero.
- All three pathway cards are equally legible and Spark is unmistakably first.
- No editorial heading clips or exceeds the content boundary.
- The final planning-call CTA is visually primary without recurring throughout the page.

### Tablet

- No card copy is reduced below the body-size floor to preserve three columns.
- Photographs retain their intended subjects at common portrait and landscape tablet ratios.
- Navigation remains clear without crowding the logo.

### Mobile

- The page has no horizontal overflow at 320 px CSS width.
- Pathway cards follow Spark → Foundation → Core in document and visual order.
- Each button is comfortably tappable and the planning-call label remains on one or two intentional lines.
- Heading wraps are manually checked at 320, 375 and 430 px widths.
- The Spark facts remain a concise list rather than becoming a dense paragraph.
- Texture never reduces text legibility.

### Accessibility and content

- Colour combinations meet WCAG AA for their actual text size and weight.
- Heading levels form one logical hierarchy.
- Keyboard focus is visible on menus, links and the CTA.
- No pathway meaning depends only on colour, texture or connector lines.
- Reduced-motion settings are respected.
- Booking opens the existing Wix planning-call journey and has no dead end.
- The published page contains no Summer Series reference.
- Spark is never described as six weekly sessions or a six-week commitment per child.

## Build and review sequence

1. Duplicate the current page and work on the unpublished copy.
2. Remove Log In from the global header while leaving the inactive member-area feature intact.
3. Establish global colours, type styles, maximum width and spacing tokens.
4. Build the seven sections with placeholder image frames only where originals are not yet accessible.
5. Construct the pathway from responsive elements.
6. Add owner-supplied logo and photography without recreating assets.
7. Test desktop, tablet and mobile acceptance criteria.
8. Test the planning-call journey.
9. Share the staged Wix preview for owner review.
10. Publish only after approval, retaining the existing URL and SEO metadata unless a migration is separately agreed.
