import type { Transport } from "@/lib/types"

export const transport: Transport[] = [
  {
    slug: "heho-airport",
    name: { en: "Heho Airport (HEH)", my: "ဟဲဟိုး လေဆိပ် (HEH)" },
    address: { en: "Heho, Shan State (dummy)", my: "ဟဲဟိုး၊ ရှမ်းပြည်နယ် (နမူနာ)" },
    phones: ["+95 81 400 2101", "+95 9 4000 2101"],
  },
  {
    slug: "taunggyi-bus-terminal",
    name: { en: "Taunggyi Bus Terminal", my: "တောင်ကြီး အဝေးပြေး ကားဂိတ်" },
    address: { en: "Bogyoke Aung San Rd (dummy)", my: "ဗိုလ်ချုပ်အောင်ဆန်းလမ်း (နမူနာ)" },
    phones: ["+95 81 400 2102", "+95 9 4000 2102"],
  },
  {
    slug: "yangon-overnight-bus",
    name: { en: "Yangon Overnight Express", my: "ရန်ကုန် ညထွက် အဝေးပြေးကား" },
    address: { en: "Gate 3, Taunggyi Bus Terminal (dummy)", my: "တောင်ကြီး ကားဂိတ်၊ ဂိတ်အမှတ် ၃ (နမူနာ)" },
    phones: ["+95 9 4000 2103"],
  },
  {
    slug: "mandalay-bus",
    name: { en: "Mandalay Express", my: "မန္တလေး အဝေးပြေးကား" },
    address: { en: "Gate 1, Taunggyi Bus Terminal (dummy)", my: "တောင်ကြီး ကားဂိတ်၊ ဂိတ်အမှတ် ၁ (နမူနာ)" },
    phones: ["+95 9 4000 2104"],
  },
  {
    slug: "city-taxi",
    name: { en: "City Taxi Stand", my: "မြို့လယ် တက္ကစီဂိတ်" },
    address: { en: "Myo Ma Market front (dummy)", my: "မြို့မဈေးရှေ့ (နမူနာ)" },
    phones: ["+95 9 4000 2105", "+95 9 4000 2115"],
  },
  {
    slug: "motorbike-taxi",
    name: { en: "Motorbike Taxi Corner", my: "မော်တော်ဆိုင်ကယ် တက္ကစီဂိတ်" },
    address: { en: "Downtown Lane 2 (dummy)", my: "မြို့လယ် လမ်းသွယ် ၂ (နမူနာ)" },
    phones: ["+95 9 4000 2106"],
  },
  {
    slug: "nyaungshwe-songthaew",
    name: { en: "Nyaungshwe Pickup", my: "ညောင်ရွှေ လိုင်းကားဂိတ်" },
    address: { en: "Southbound stop, Market (dummy)", my: "ဈေးအနီး တောင်ဘက်လိုင်းကားမှတ်တိုင် (နမူနာ)" },
    phones: ["+95 9 4000 2107"],
  },
  {
    slug: "festival-shuttle",
    name: { en: "Festival Shuttle Stand", my: "ပွဲတော်ကွင်း ကြိုပို့ယာဉ်ဂိတ်" },
    address: { en: "Sports Ground Gate (dummy)", my: "အားကစားကွင်း ဂိတ်ပေါက် (နမူနာ)" },
    phones: ["+95 9 4000 2108"],
  },
]