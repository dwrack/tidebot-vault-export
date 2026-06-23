# FAQ Schema — Ready to Deploy (/faq)

Verified June 22 2026: the /faq page has NO FAQPage schema live (only the site-wide DaySpa block rides in the header). This deploys it.

## Deploy steps
1. Make the visible-page edits below first (Squarespace → Pages → /faq → edit the accordion). Schema content MUST match what visitors see, or Google can issue a manual action.
2. Then paste the JSON block into **Pages → /faq → Page Settings (gear) → Advanced → Page Header Code Injection**. Page-level, not site-level.
3. Validate at https://search.google.com/test/rich-results using the /faq URL. Rich results take 1-2 weeks to show.

## Visible-page edits (do these in the accordion FIRST)
- **Location answer** → replace with the Vancouver/Hayden Island version (matches Q1 below).
- **River-temperature answer** → replace the "Click here" text with the real seasonal answer (matches Q20 below).
- **Delete the duplicate** "What are the sauna hours?" accordion item (it appears twice).
- **Add 6 new accordion items**: cost, swimsuit/clothing, cold plunge temp, private events, Vancouver, gift cards (Q26-Q31 below).

> Pricing in Q26 uses social $59/seat, private $539, membership $99/mo. Confirm these are current before publishing.

## Paste this into /faq Page Header Code Injection

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is Ebb & Ember located?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We are on the Oregon shore of North Portland at Elevated Tides Marina, 173 NE Bridgeton Road, Portland, OR 97211, right on the Columbia River. We sit directly across the river from Vancouver, Washington, about a 10 to 15 minute drive from downtown Vancouver over the I-5 or I-205 bridge. We are near Hayden Island and PDX airport, with free parking on site."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a sauna near Vancouver, Washington?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Ebb & Ember is a floating sauna and cold plunge on the Columbia River in North Portland, directly across from Vancouver, WA. We are about a 10 to 15 minute drive from downtown Vancouver over the I-5 or I-205 bridge, with free parking on site."
      }
    },
    {
      "@type": "Question",
      "name": "How much does a sauna session cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Social sessions, where you share the sauna with other guests, start at $59 per person. Private sessions for your own group start at $539 and hold up to 10 guests. We also offer monthly memberships starting at $99. Book any session through our website."
      }
    },
    {
      "@type": "Question",
      "name": "Do I wear a swimsuit, or is it clothing-optional?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For social, shared sessions a swimsuit is required. For private bookings, what your group wears is up to you. Either way, bring a swimsuit so you can use the cold plunge."
      }
    },
    {
      "@type": "Question",
      "name": "How cold is the cold plunge and Columbia River year-round?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Columbia is Cascade snowmelt, so it shifts with the seasons. It runs around 42 degrees Fahrenheit in winter, climbs into the 50s in spring, reaches the mid 60s in summer, and cools back through fall. The plunge is always optional, and a cold shower is available if you prefer."
      }
    },
    {
      "@type": "Question",
      "name": "Can I book the sauna for a private event or party?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A private session books the whole sauna for your group, up to 10 guests, with the rooftop deck and locker lounge to yourselves. It is popular for birthdays, team outings, and small celebrations. Book a private session on our website or email sauna@ebbandember.com."
      }
    },
    {
      "@type": "Question",
      "name": "Do you sell gift cards?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Sauna and cold plunge gift cards are available for both social and private sessions through the shop on our website. They make an easy gift for anyone in the Portland or Vancouver area."
      }
    },
    {
      "@type": "Question",
      "name": "What should I expect on my first visit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Arrive in your session window, change in the locker lounge, then cycle between the cedar sauna and the cold Columbia or a cold shower. It is a self-guided experience with free parking on site. Bring a swimsuit, two towels, and a water bottle."
      }
    },
    {
      "@type": "Question",
      "name": "Are you open year-round, even in winter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We run sessions seven days a week, all year. Winter is one of the best times to go: the sauna stays hot, the Columbia is at its coldest for a sharp contrast plunge, and steam off the river is part of the experience."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to book in advance, or can I walk in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We recommend booking online in advance. Because the sauna is a self-guided experience and entry is by door code, walk-ins are not guaranteed and popular times often sell out. Reserve your session on our website."
      }
    },
    {
      "@type": "Question",
      "name": "What are the benefits of a sauna and cold plunge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Guests come for the hot-cold contrast ritual: the deep heat of the cedar sauna followed by a cold plunge in the Columbia. People describe it as relaxing, restorative, and energizing, a way to reset, sleep better, and feel clear-headed. Cycle between hot and cold as many times as you like during your session."
      }
    },
    {
      "@type": "Question",
      "name": "What makes Ebb & Ember different from other saunas in Portland?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ebb & Ember is Portland's floating sauna, a cedar sauna boat docked on the Columbia River where your cold plunge is the actual river, not a tub. You get rooftop deck views, real snowmelt cold water, and a self-guided experience just across from Vancouver, WA. It is the only sauna of its kind in the area."
      }
    },
    {
      "@type": "Question",
      "name": "What are the sauna hours?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We run sessions daily from 7am to 9pm. Each session is 1 hour and 45 minutes plus a 15 minute transition. Off-peak is Monday through Thursday all day and Friday before 5pm. Peak is Friday 5pm through Sunday plus holidays."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to be on time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The sauna stays docked at all times, so you can arrive anywhere within your session window. No need to be there exactly at the start."
      }
    },
    {
      "@type": "Question",
      "name": "What should I bring?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A swimsuit, two towels (one to sit on and one to dry off), a non-metallic water bottle, and inside-only sandals with clean soles. You are also welcome to go barefoot."
      }
    },
    {
      "@type": "Question",
      "name": "Are towels and robes provided, or should I bring my own?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We do not currently provide towels or robes. Please bring two towels: one to sit on in the sauna and one to use after showering or cold plunging."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a place to fill up my water bottle?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. There is a filtered water station in the locker lounge to refill your water bottle."
      }
    },
    {
      "@type": "Question",
      "name": "Can we bring food or snacks for our session?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You are welcome to bring snacks for the rooftop or lounge during your visit. For safety and cleanliness, we ask that only water be brought inside the sauna."
      }
    },
    {
      "@type": "Question",
      "name": "Are there showers or bathrooms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Freshwater rinse showers are on the boat, though soap is not allowed there for environmental reasons. The locker lounge on the dock has a bathroom and a heated shower with premium toiletries."
      }
    },
    {
      "@type": "Question",
      "name": "Is there anywhere to hang out outside?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. There is a rooftop deck on the sauna and a covered locker lounge on the dock to relax and take in the views. The lounge has a bathroom, shower, lockers, shoe cubbies, and a countertop for snacks and drinks."
      }
    },
    {
      "@type": "Question",
      "name": "Can I come if it is raining?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Rain and mist only enhance the experience, and the ember always glows. Bookings are not cancelled due to weather."
      }
    },
    {
      "@type": "Question",
      "name": "Do you have a lost and found?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Email sauna@ebbandember.com if you left something behind. Unclaimed items are donated every two weeks."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a safe place to store my stuff?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. We have keyed lockers on site as well as open cubbies."
      }
    },
    {
      "@type": "Question",
      "name": "Is there staff onsite?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Ebb & Ember is a self-guided experience. Reach us anytime at sauna@ebbandember.com or (503) 308-1293."
      }
    },
    {
      "@type": "Question",
      "name": "Are kids allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Children ages 13 and up are welcome for private bookings only, with a parent or legal guardian present who has signed a waiver for the child. Social bookings are for guests 18 and older."
      }
    },
    {
      "@type": "Question",
      "name": "Can I plunge into the river?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the cold plunge is part of the experience and always optional. There is no lifeguard on duty, so you enter at your own risk. This is an active marina with currents, boat traffic, and changing conditions, so use the buddy system and the platform ladders when exiting the water."
      }
    },
    {
      "@type": "Question",
      "name": "What if I am pregnant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We do not recommend using the sauna while pregnant. Please consult your physician. You are still welcome to enjoy the rest of the boat, locker lounge, and landing area."
      }
    },
    {
      "@type": "Question",
      "name": "Are animals allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Service animals only. For the safety and comfort of all guests, pets are not permitted in the sauna facilities. The high heat and humidity are unsafe for animals."
      }
    },
    {
      "@type": "Question",
      "name": "What kind of sauna is it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is a propane-fired cedar sauna that can be wet or dry depending on how much water you add to the stones."
      }
    },
    {
      "@type": "Question",
      "name": "How hot does it get?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The sauna heats to about 190 degrees Fahrenheit, then cycles off and back on around 170 degrees. You may hear a metal expansion sound during those temperature changes. It is part of the process."
      }
    },
    {
      "@type": "Question",
      "name": "How do I change my booking time or day?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open your confirmation email and click change booking at the bottom. From there you can move your booking to another time, or cancel to receive a gift card code. The gift card code is stored in your booking info for future use."
      }
    },
    {
      "@type": "Question",
      "name": "What does social sauna mean?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A social session is a shared community sauna. Guests from different groups book the same time slot and enjoy the sauna together. Conversation and meeting new people are part of the atmosphere, though many guests simply relax quietly while sharing the space."
      }
    },
    {
      "@type": "Question",
      "name": "How many people fit in the sauna at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Up to 8 guests in a day-to-day social session. If you book the social sauna as a private party, up to 10 guests."
      }
    },
    {
      "@type": "Question",
      "name": "What if I have a question about a private booking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A private booking holds up to 10 guests and can be as few as 1. The door code is sent once all waivers are signed. To adjust party size, open your booking and reduce the number of guests, or have everyone re-sign the waiver to cover empty spots. Email sauna@ebbandember.com for help."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get a refund?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All sales are final. You can cancel your booking to receive a gift card code and use it for another time or person. To cancel, open your confirmation email, click change booking, then cancel booking to get your gift card code."
      }
    }
  ]
}
</script>
```
