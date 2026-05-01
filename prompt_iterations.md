# Prompt Iterations

Three iterations tested against both `sample_transcript_assignment_1.txt` and `sample_transcript_assignment_2.txt`. Model: `openai/gpt-oss-120b` on Groq, `temperature=0.2`, `max_tokens=1500`.


## Iteration 1 - Plain natural language ask

**Prompt:**
```text
Read the following interview transcript and summarize it. I need three things:
1. Topics covered
2. What kind of profile/role they fit (with a brief justification from the conversation)
3. A short candidate summary paragraph (3-6 sentences) outlining their background, strengths, notable concerns and overall impression.
```

**Input (excerpt - transcript 1):**
```
[13:06] Candidate: Hi sir. My name is Prasanna Kumar. I have around nine plus years
of experience ... My core technical expertise is on Angular, React and Ionic framework.
I'm working with the backend by using Node.js, Express and .NET Core.
...
[55:01] Interviewer: Have you used Zustand?
[55:05] Candidate: Zustand, I cannot use this. I worked on React Query.
[55:14] Interviewer: Can you write an example of Zustand for creating a useStore?
[55:24] Candidate: Yeah. Like a constant. Use store. This is the base structure.
```

**Output (full - transcript 1):**
```
**1. Topics Covered**

- AI‑assisted software development (Cursor, GitHub Copilot, Claude) – how to use an assistant throughout the feature lifecycle.
- Hybrid mobile development with **Ionic 7**, Angular, React, and Capacitor (camera, filesystem, network plugins).
- UI/UX and performance strategies for mobile‑first dashboards: feature‑based modules, reusable components, Ionic Grid/Flexbox, virtual scroll, lazy loading, bundle‑size optimisation.
- CSS‑utility framework **Tailwind CSS** – configuration, theming, `@apply`, mobile‑first break‑points, global design system.
- Scalable **Angular** architecture for enterprise dashboards (core, shared, feature modules, lazy loading, interceptors, NgRx vs RxJS).
- **React** state‑management patterns for large apps (Context + Reducer, React Query, Redux Toolkit `createSlice`; brief discussion of Zustand).
- Backend integration basics (Node.js/Express, .NET Core services, CRUD services, error handling, retry logic).
- General software‑engineering concerns: requirement analysis, team composition, testing on emulators/devices, handling large data sets, and synchronization of offline data.

---

**2. Profile / Role Fit (with justification)**

**Senior Full‑Stack Mobile Engineer / Hybrid‑App Lead**
- **Experience:** 9 + years in software development, with a focus on Angular, React, and Ionic/Capacitor.
- **Technical breadth:** Comfortable designing both front‑end (feature modules, reusable UI, state management) and back‑end (Node.js, .NET Core services).
- **Hybrid expertise:** Demonstrated end‑to‑end knowledge of building, deploying, and optimizing Ionic/Capacitor apps for iOS & Android.
- **Modern practices:** Uses AI‑coding assistants, Tailwind utility‑first styling, lazy‑loading, virtual scroll, and CI‑friendly modular architecture.
- **Leadership potential:** Talks about architecture planning, team skill‑mapping, and parallel front‑end/back‑end development, indicating readiness to own larger projects or mentor junior staff.

---

**3. Candidate Summary (3‑6 sentences)**

Prasanna Kumar is a 9‑year veteran software developer whose core strengths lie in hybrid mobile development with Ionic, Angular, and React, complemented by solid backend experience in Node.js and .NET Core. He articulates a clear, modular approach to building scalable, performance‑focused applications, leveraging AI‑assisted coding tools, Tailwind CSS, and modern state‑management solutions such as React Query and Redux Toolkit. While he shows confidence in most areas, he is less familiar with Zustand and needed prompting for some code snippets, suggesting a slight gap in the broader React ecosystem. Overall, he presents as a capable senior/full‑stack mobile engineer ready to lead complex cross‑platform projects, with a strong emphasis on architecture, reusability, and AI‑enhanced productivity.
```

**What worked / what didn't:**
The model picked up the right content, but with no set schema or structure provided, it used the shape numbered section headings (`**1. Topics Covered**`), and a Profile section with free-form sub-bullets (`Experience:`, `Technical breadth:`, `Leadership potential:`) and it provided different structure on every run, making summaries hard to compare side-by-side. It also provided information beyond the transcript: the "Leadership potential: and readiness to own larger projects or mentor junior staff" line is invented as the candidate never discusses leadership or mentoring. Re-running the same prompt (and on transcript 2) produced different structures including markdown tables and multiple suggested roles. Overall, it was providing a hard summary of the conversation instead of judging and providing it with the conclusions.

---

## Iteration 2 - Recruiter persona + section labels

**Prompt:**
```text
Act as an expert technical recruiter. Analyze tehe transcript and provide:
**Topics covered**: Bulleted list.
**Profile**: State the role and seniority (e.g., Backend Engineer - Mid-level),
followed by a brief justification.
**Candidate summary**: 3-6 sentences covering background, strengths, concerns,
and overall impression.
```

**Input (excerpt - transcript 2):**
```
[3:31] Candidate: Myself Krishna. From Telangana, Hyderabad. B.Tech in mechanical
engineering, 2018.
[4:05] Candidate: In 2019 I joined an ed-tech company as associate in operations.
...
[5:01] Candidate: Then promoted into a new department — FDPU, fraud detection
and prevention unit.
...
[61:59] Interviewer: You use lot of jargons in Hindi when you try to explain.
In starting round fine, but as rounds increase it will be about communication
and confidence.
```

**Output (full - transcript 2):**
```
**Topics covered**
- Interview structure & role framing (project‑program manager, vendor & stakeholder engagement)
- Candidate background – education, early career in ed‑tech operations & digital finance
- Fraud‑Detection & Prevention Unit (FDPU) – building CRM, ISO certification, risk‑score model, vendor onboarding
- End‑to‑end initiative: loan‑payment fraud mitigation (credit‑bureau integration, bank partnerships, data enrichment, scoring)
- Vendor selection, onboarding, performance management, escalation & termination process
- Cross‑functional alignment for mis‑aligned product/UI/software teams (phased rollout, cadence meetings)
- BPO / call‑center efficiency improvements (auto‑dialer, predictive dialing, UI shortcuts)
- Operational KPIs (dialer activity, talk time, revenue, ROAS, CAC, retention) and incentive linkage
- Executive reporting – weekly/monthly business reviews, dashboards, data validation & stakeholder disagreement handling
- Prioritisation of competing stakeholder requests and communication of trade‑offs
- Measuring success in multi‑party projects and taking ownership of outcomes
- Feedback on communication style (use of Hindi jargon) and confidence for senior leadership interaction

**Profile**
**Senior Program / Operations Manager – 6‑8 years experience**
Krishna has progressed from an associate in operations to leading a fraud‑detection unit, driving CRM implementations, vendor management, and analytics across two ed‑tech firms. The breadth of end‑to‑end project ownership, stakeholder‑level reporting, and cross‑functional coordination aligns with a senior‑level program‑management role rather than an entry‑level coordinator.

**Candidate summary**
Krishna holds a B.Tech in Mechanical Engineering (2018) and has accumulated roughly eight years of experience in operations, finance, fraud detection, and analytics within the ed‑tech sector. He demonstrates strong end‑to‑end delivery skills—designing risk‑scoring models, integrating with banks and credit bureaus, and launching company‑wide CRMs—while also managing vendor relationships from selection through termination. His KPI‑driven approach and regular executive dashboards show solid analytical capability, though his reliance on Hindi‑mixed jargon and occasional confidence gaps could hinder senior‑leadership interactions. Overall, he appears capable of handling a hybrid project‑program and vendor‑management function, provided he refines his executive communication style.
```

**What worked / what didn't:**
The format was much tighter and section labels, bullets were consistent, and the summary length was good. Two issues were there: First, the model provided incorrect tenure: the transcript says he joined in 2019 (~6 years to mid-2025), but the output rounded up to "roughly eight years" and the profile line says a "6-8 years experience" qualifier I never asked for. Second, the persona tempted the model to add extra `Interview structure & role framing` topic that's about the interviewer, not the candidate.

---

## Iteration 3 - Strict template + evidence guard (final)

**Prompt:**
```text
You are an expert technical recruiter and hiring manager. Your task is to analyze
the provided interview transcript and generate a structured summary.

You must output EXACTLY three sections formatted exactly as follows, with no extra
introductory or concluding conversational text:

**Topics covered**
- [Bullet points of main themes, technical concepts, or behavioral topics discussed]

**Profile**
[Role/Title] - [Seniority Level]
Justification: [1-2 sentences explaining why based strictly on the transcript evidence]

**Candidate summary**
[A single short paragraph of 3-6 sentences detailing their background, core strengths,
notable concerns or areas of friction, and an overall impression.]
```

**Input (excerpts):**

*Transcript 1 - same Prasanna excerpt as iteration 1.*

*Transcript 2 - same Krishna excerpt as iteration 2.*

**Output (full - transcript 1):**
```
**Topics covered**
- AI‑assisted software development (using tools like Cursor, GitHub Copilot, Claude)
- Mobile app development with Ionic 7, Angular, Capacitor, and Cordova
- Handling large data sets (virtual scroll, pagination, lazy loading) and performance optimization
- Capacitor plugin ecosystem for native features (camera, filesystem, network)
- Tailwind CSS utility‑first styling and design system scalability
- Scalable Angular architecture (feature modules, core/shared modules, lazy loading, NgRx/ RxJS)
- React state‑management strategies (Context API, reducers, React Query, Redux Toolkit, brief mention of Zustand)
- Writing TypeScript Redux slices and basic store patterns

**Profile**
Senior Front‑End / Full‑Stack Engineer – Senior
Justification: The candidate has ~9 years of software development experience, deep expertise in Angular, React, Ionic, and backend work with Node.js/.NET Core, and demonstrates architectural knowledge across mobile, web, and state‑management frameworks, indicating a senior‑level role.

**Candidate summary**
The candidate is a seasoned developer with nine years of experience building service‑based, risk‑assessment, and communication applications using Angular, React, and Ionic, complemented by backend skills in Node.js and .NET Core. They show strong practical knowledge of AI‑assisted coding tools, mobile‑first UI design, Capacitor native plugins, and performance techniques for large data sets. Their approach to styling with Tailwind and modular architecture in both Angular and React reflects a solid grasp of scalable front‑end engineering. While comfortable with Redux Toolkit and React Query, they have limited exposure to Zustand. Overall, the candidate appears technically proficient, articulate, and well‑suited for senior front‑end or full‑stack positions.
```

**Output (full - transcript 2):**
```
**Topics covered**
- Program and project management across ed‑tech operations
- Vendor selection, onboarding, performance monitoring, and escalation
- Fraud detection and prevention workflow design, risk scoring, and ISO certification
- CRM implementation (Merito), BRD/PRD creation, and integration with payment gateways and telecom APIs
- Business analytics, dashboard creation, KPI definition for sales, marketing, and operations
- Process improvement for BPO/calling efficiency (auto‑dialer, predictive dialing)
- Stakeholder communication, data presentation to senior leadership, and handling data disputes
- Prioritization and decision‑making when multiple stakeholders request conflicting work

**Profile**
Program/Operations Manager – Mid‑Senior Level
Justification: The candidate describes leading end‑to‑end initiatives (fraud detection unit, CRM rollout, vendor management), managing cross‑functional teams, presenting executive dashboards, and influencing senior leadership, indicating a managerial role with several years of experience beyond entry level.

**Candidate summary**
Krishna holds a B.Tech in Mechanical Engineering and has progressed from an associate operations role in 2019 to managing fraud detection, vendor relationships, and business analytics in ed‑tech firms. His core strengths lie in building and scaling processes—such as implementing a risk‑scoring model, driving CRM adoption, and optimizing BPO call workflows—while effectively communicating data to senior stakeholders. He demonstrates solid program‑management skills, KPI‑driven performance tracking, and the ability to navigate complex vendor ecosystems. Areas of concern include occasional reliance on Hindi jargon, which may affect clarity in senior‑level interactions. Overall, he appears capable of handling a hybrid project‑program and vendor‑management function with a focus on operational efficiency.
```

**What worked / what didn't:**
The strict template eliminated the format drift from iteration 1 and the extra unnecessary information from iteration 2 both transcripts now produce the same three sections, with seniority called out on a single line. The "based strictly on the transcript evidence" prompt removed the incorrect tenure prediction: transcript 2 went from "roughly eight years" (iter 2) to a "progressed from an associate operations role in 2019" with a hedged "Mid-Senior Level" instead of an year range. The remaining limitation is that for the technical transcript the model still picks a slightly hybrid title ("Senior Front-End / Full-Stack Engineer - Senior") rather than committing a future iteration could force a single canonical role string, but for both summaries the output is now consumable and easily comparable.
