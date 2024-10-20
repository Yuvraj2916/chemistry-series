import time

i=0

while i<1:

    d1={'Hydrogen':('Hydrogen is the chemical element with the symbol H and atomic number 1. Hydrogen is the lightest element. At standard conditions hydrogen is a gas of diatomic molecules having the formula H2. It is colorless, odorless, tasteless, non-toxic, and highly combustible.In the early universe, the formation of protons, the nuclei of hydrogen, occurred during the first second after the Big Bang. The emergence of neutral hydrogen atoms throughout the universe occurred about 370,000 years later during the recombination epoch, when the plasma had cooled enough for electrons to remain bound to protons.')

        ,'Helium':('Helium is a chemical element with the symbol He and atomic number 2. It is a colorless, odorless, tasteless, non-toxic, inert, monatomic gas and the first in the noble gas group in the periodic table.Its boiling and melting point are the lowest among all the elements.')

        ,'Lithium':("Lithium is a chemical element with the symbol Li and atomic number 3. It is a soft, silvery-white alkali metal. Under standard conditions, it is the least dense metal and the least dense solid element. Like all alkali metals, lithium is highly reactive and flammable, and must be stored in vacuum, inert atmosphere, or inert liquid such as purified kerosene or mineral oil. ")

        ,'Beryllium':("Beryllium is a chemical element with the symbol Be and atomic number 4. It is a steel-gray, strong, lightweight and brittle alkaline earth metal. It is a divalent element that occurs naturally only in combination with other elements to form minerals.It is a relatively rare element in the universe, usually occurring as a product of the spallation of larger atomic nuclei that have collided with cosmic rays.")

        ,'Boron':("Boron is a chemical element with the symbol B and atomic number 5. In its crystalline form it is a brittle, dark, lustrous metalloid; in its amorphous form it is a brown powder. As the lightest element of the boron group it has three valence electrons for forming covalent bonds, resulting in many compounds such as boric acid, the mineral sodium borate, and the ultra-hard crystals of boron carbide and boron nitride.")

        ,'Carbon':("Carbon is a chemical element with the symbol C and atomic number 6. It is nonmetallic and tetravalent—its atom making four electrons available to form covalent chemical bonds. It belongs to group 14 of the periodic table. Carbon makes up only about 0.025 percent of Earth's crust. Three isotopes occur naturally, 12C and 13C being stable, while 14C is a radionuclide, decaying with a half-life of about 5,730 years. Carbon is one of the few elements known since antiquity.")

        ,'Nitrogen':("Nitrogen is the chemical element with the symbol N and atomic number 7. Nitrogen is a nonmetal and the lightest member of group 15 of the periodic table, often called the pnictogens. It is a common element in the universe, estimated at seventh in total abundance in the Milky Way and the Solar System. At standard temperature and pressure, two atoms of the element bond to form N2, a colorless and odorless diatomic gas. N2 forms about 78% of Earth's atmosphere, making it the most abundant uncombined element.")

        ,'Oxygen':("Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. Oxygen is Earth's most abundant element, and after hydrogen and helium, it is the third-most abundant element in the universe. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O2") 

        ,'Fluorine':("Fluorine is a chemical element with the symbol F and atomic number 9. It is the lightest halogen and exists at standard conditions as a highly toxic, pale yellow diatomic gas. As the most electronegative element, it is extremely reactive, as it reacts with all other elements except for argon, neon, and helium.")

        ,'Neon':("Neon is a chemical element with the symbol Ne and atomic number 10. It is a noble gas. Neon is a colorless, odorless, inert monatomic gas under standard conditions, with about two-thirds the density of air. It was discovered (along with krypton and xenon) in 1898 as one of the three residual rare inert elements remaining in dry air, after nitrogen, oxygen, argon and carbon dioxide were removed. Neon was the second of these three rare gases to be discovered and was immediately recognized as a new element from its bright red emission spectrum.")

        ,'Sodium':("Sodium is a chemical element with the symbol Na and atomic number 11. It is a soft, silvery-white, highly reactive metal. Sodium is an alkali metal, being in group 1 of the periodic table. The free metal does not occur in nature, and must be prepared from compounds. Sodium is the sixth most abundant element in the Earth's crust and exists in numerous minerals such as feldspars, sodalite, and halite")

        ,'Magnesium':("Magnesium is a chemical element with the symbol Mg and atomic number 12. It is a shiny gray solid which shares many physical and chemical properties with the other five alkaline earth metals.This element is produced in large, aging stars from the sequential addition of three helium nuclei to a carbon nucleus. When such stars explode as supernovas, much of the magnesium is expelled into the interstellar medium where it may recycle into new star systems.")

        ,'Aluminium':("Aluminium is a chemical element with the symbol Al and atomic number 13. Aluminium has a density lower than those of other common metals, at approximately one third that of steel. It has a great affinity towards oxygen, and forms a protective layer of oxide on the surface when exposed to air. Aluminium visually resembles silver, both in its color and in its great ability to reflect light. It is soft, non-magnetic and ductile.")

        ,'Silicon':("Silicon is a chemical element with the symbol Si and atomic number 14. It is a hard, brittle crystalline solid with a blue-grey metallic luster, and is a tetravalent metalloid and semiconductor. It is a member of group 14 in the periodic table: carbon is above it; and germanium, tin, lead, and flerovium are below it. It is relatively unreactive.")

        ,'Phosphorus':("Phosphorus is a chemical element with the symbol P and atomic number 15. Elemental phosphorus exists in two major forms, white phosphorus and red phosphorus, but because it is highly reactive, phosphorus is never found as a free element on Earth. It has a concentration in the Earth's crust of about one gram per kilogram . In minerals, phosphorus generally occurs as phosphate.")

        ,'Sulfur':("Sulfur (or sulphur in British English) is a chemical element with the symbol S and atomic number 16. It is abundant, multivalent and nonmetallic. Under normal conditions, sulfur atoms form cyclic octatomic molecules with a chemical formula . Elemental sulfur is a bright yellow, crystalline solid at room temperature.")

        ,'Chlorine':("Chlorine is a chemical element with the symbol Cl and atomic number 17. The second-lightest of the halogens, it appears between fluorine and bromine in the periodic table and its properties are mostly intermediate between them. Chlorine is a yellow-green gas at room temperature. It is an extremely reactive element and a strong oxidising agent: among the elements, it has the highest electron affinity and the third-highest electronegativity on the revised Pauling scale, behind only oxygen and fluorine.")

        ,'Argon':("Argon is a chemical element with the symbol Ar and atomic number 18. It is in group 18 of the periodic table and is a noble gas. Argon is the third-most abundant gas in Earth's atmosphere, at 0.934% (9340 ppmv). It is more than twice as abundant as water vapor (which averages about 4000 ppmv, but varies greatly), 23 times as abundant as carbon dioxide (400 ppmv), and more than 500 times as abundant as neon (18 ppmv). Argon is the most abundant noble gas in Earth's crust, comprising 0.00015% of the crust.")

        ,'Potassium':("Potassium is the chemical element with the symbol K and atomic number 19. Potassium is a silvery-white metal that is soft enough to be cut with a knife with little force. Potassium metal reacts rapidly with atmospheric oxygen to form flaky white potassium peroxide in only seconds of exposure. It was first isolated from potash, the ashes of plants, from which its name derives. In the periodic table, potassium is one of the alkali metals, all of which have a single valence electron in the outer electron shell, that is easily removed to create an ion with a positive charge – a cation, that combines with anions to form salts.")

        ,'Calcium':("Calcium is a chemical element with the symbol Ca and atomic number 20. As an alkaline earth metal, calcium is a reactive metal that forms a dark oxide-nitride layer when exposed to air. Its physical and chemical properties are most similar to its heavier homologues strontium and barium. It is the fifth most abundant element in Earth's crust, and the third most abundant metal, after iron and aluminium. The most common calcium compound on Earth is calcium carbonate, found in limestone and the fossilised remnants of early sea life; gypsum, anhydrite, fluorite, and apatite are also sources of calcium.")

        ,'Scandium':("Scandium is a chemical element with the symbol Sc and atomic number 21. It is a silvery-white metallic d-block element. Historically, it has been classified as a rare-earth element,together with yttrium and the Lanthanides. It was discovered in 1879 by spectral analysis of the minerals euxenite and gadolinite from Scandinavia.Scandium is present in most of the deposits of rare-earth and uranium compounds, but it is extracted from these ores in only a few mines worldwide. Because of the low availability and difficulties in the preparation of metallic scandium, which was first done in 1937, applications for scandium were not developed until the 1970s, when the positive effects of scandium on aluminium alloys were discovered, and its use in such alloys remains its only major application.")

        ,'Titanium':("Titanium is a chemical element with the symbol Ti and atomic number 22. Found in nature only as an oxide, it can be reduced to produce a lustrous transition metal with a silver color, low density, and high strength, resistant to corrosion in sea water, aqua regia, and chlorine.Titanium was discovered in Cornwall, Great Britain, by William Gregor in 1791 and was named by Martin Heinrich Klaproth after the Titans of Greek mythology.")

        ,'Vanadium':("Vanadium is a chemical element with the symbol V and atomic number 23. It is a hard, silvery-grey, malleable transition metal. The elemental metal is rarely found in nature, but once isolated artificially, the formation of an oxide layer somewhat stabilizes the free metal against further oxidation. Spanish scientist Andrés Manuel del Río discovered compounds of vanadium in 1801 in Mexico by analyzing a new lead-bearing mineral he called 'brown lead'.")

        ,'Chromium':("Chromium is a chemical element with the symbol Cr and atomic number 24. It is the first element in group 6. It is a steely-grey, lustrous, hard, and brittle transition metal.Chromium metal is valued for its high corrosion resistance and hardness. A major development in steel production was the discovery that steel could be made highly resistant to corrosion and discoloration by adding metallic chromium to form stainless steel.")

        ,'Manganese':("Manganese is a chemical element with the symbol Mn and atomic number 25. It is a hard, brittle, silvery metal, often found in minerals in combination with iron. Manganese is a transition metal with a multifaceted array of industrial alloy uses, particularly in stainless steels. It improves strength, workability, and resistance to wear. Manganese oxide is used as an oxidising agent; as a rubber additive; and in glass making, fertilisers, and ceramics. Manganese sulfate can be used as a fungicide.")

        ,'Iron':("Iron is a chemical element with symbol Fe and atomic number 26. It is a metal that belongs to the first transition series and group 8 of the periodic table. It is, by mass, the most common element on Earth, right in front of oxygen , forming much of Earth's outer and inner core. It is the fourth most common element in the Earth's crust.")

        ,'Cobalt':("Cobalt is a chemical element with the symbol Co and atomic number 27. As with nickel, cobalt is found in the Earth's crust only in a chemically combined form, save for small deposits found in alloys of natural meteoric iron. The free element, produced by reductive smelting, is a hard, lustrous, silver-gray metal.")

        ,'Nickel':("Nickel is a chemical element with symbol Ni and atomic number 28. It is a silvery-white lustrous metal with a slight golden tinge. Nickel is a hard and ductile transition metal. Pure nickel is chemically reactive but large pieces are slow to react with air under standard conditions because a passivation layer of nickel oxide forms on the surface that prevents further corrosion. Even so, pure native nickel is found in Earth's crust only in tiny amounts, usually in ultramafic rocks, and in the interiors of larger nickel–iron meteorites that were not exposed to oxygen when outside Earth's atmosphere.")

        ,'Copper':("Copper is a chemical element with the symbol Cu and atomic number 29. It is a soft, malleable, and ductile metal with very high thermal and electrical conductivity. A freshly exposed surface of pure copper has a pinkish-orange color. Copper is used as a conductor of heat and electricity, as a building material, and as a constituent of various metal alloys, such as sterling silver used in jewelry, cupronickel used to make marine hardware and coins, and constantan used in strain gauges and thermocouples for temperature measurement")

        ,'Zinc':("Zinc is a chemical element with the symbol Zn and atomic number 30. Zinc is a slightly brittle metal at room temperature and has a shiny-greyish appearance when oxidation is removed. It is the first element in group 12 of the periodic table. In some respects, zinc is chemically similar to magnesium")

        ,'Gallium':("Gallium is a chemical element with the symbol Ga and atomic number 31. Discovered by French chemist Paul-Émile Lecoq de Boisbaudran in 1875, Gallium is in group 13 of the periodic table and is similar to the other metals of the group . Gallium exhibits relatively less similarity with boron due to latter being small in atomic size and lacking its reach to d-orbital.")

        ,'Germanium':("Germanium is a chemical element with the symbol Ge and atomic number 32. It is a lustrous, hard-brittle, grayish-white metalloid in the carbon group, chemically similar to its group neighbors silicon and tin. Pure germanium is an indirect semiconductor with an appearance similar to elemental silicon. Like silicon, germanium naturally reacts and forms complexes with oxygen in nature.")

        ,'Arsenic':("Arsenic is a chemical element with the symbol As and atomic number 33. Arsenic occurs in many minerals, usually in combination with sulfur and metals, but also as a pure elemental crystal. Arsenic is a metalloid. It has various allotropes, but only the gray form, which has a metallic appearance, is important to industry.")

        ,'Selenium':("Selenium is a chemical element with the symbol Se and atomic number 34. It is a nonmetal with properties that are intermediate between the elements above and below in the periodic table, sulfur and tellurium, and also has similarities to arsenic. It seldom occurs in its elemental state or as pure ore compounds in the Earth's crust.")

        ,'Bromine':("Bromine is a chemical element with the symbol Br and atomic number 35. It is the third-lightest element in group 17 of the periodic table and is a volatile red-brown liquid at room temperature that evaporates readily to form a similarly coloured vapour. Its properties are intermediate between those of chlorine and iodine.")

        ,'Krypton':("Krypton is a chemical element with the symbol Kr and atomic number 36. It is a colorless, odorless, tasteless noble gas that occurs in trace amounts in the atmosphere and is often used with other rare gases in fluorescent lamps. With rare exceptions, krypton is chemically inert.")

        ,'Rubidium':("Rubidium is the chemical element with the symbol Rb and atomic number 37. It is a very soft, whitish-grey solid in the alkali metal group, similar to potassium and caesium. Rubidium is the first alkali metal in the group to have a density higher than water. On Earth, natural rubidium comprises two isotopes: 72% is a stable isotope , and 28% is slightly radioactive , with a half-life of 48.8 billion years—more than three times as long as the estimated age of the universe.")

        ,'Strontium':("Strontium is the chemical element with the symbol Sr and atomic number 38. An alkaline earth metal, strontium is a soft silver-white yellowish metallic element that is highly chemically reactive. The metal forms a dark oxide layer when it is exposed to air. Strontium has physical and chemical properties similar to those of its two vertical neighbors in the periodic table, calcium and barium. It occurs naturally mainly in the minerals celestine and strontianite, and is mostly mined from these.")

        ,'Yttrium':("Yttrium is a chemical element with the symbol Y and atomic number 39. It is a silvery-metallic transition metal chemically similar to the lanthanides and has often been classified as a 'rare-earth element'. Yttrium is almost always found in combination with lanthanide elements in rare-earth minerals, and is never found in nature as a free element. 89Y is the only stable isotope, and the only isotope found in the Earth's crust.")

        ,'Zirconium':("Zirconium is a chemical element with the symbol Zr and atomic number 40. The name zirconium is taken from the name of the mineral zircon, the most important source of zirconium.")

        ,'Niobium':("Niobium is a chemical element with chemical symbol Nb and atomic number 41. It is a light grey, crystalline, and ductile transition metal. Pure niobium has a Mohs hardness rating similar to pure titanium, and it has similar ductility to iron. Niobium oxidizes in Earth's atmosphere very slowly, hence its application in jewelry as a hypoallergenic alternative to nickel.")

        ,'Molybdenum':("Molybdenum is a chemical element with the symbol Mo and atomic number 42 which is located in period 5 and group 6. The name is from Neo-Latin molybdaenum, which is based on Ancient Greek Μόλυβδος molybdos, meaning lead, since its ores were confused with lead ores. Molybdenum minerals have been known throughout history, but the element was discovered in 1778 by Carl Wilhelm Scheele.")

        ,'Technetium':("Technetium is a chemical element with the symbol Tc and atomic number 43. It is the lightest element whose isotopes are all radioactive. Nearly all available technetium is produced as a synthetic element. Naturally occurring technetium is a spontaneous fission product in uranium ore and thorium ore, the most common source, or the product of neutron capture in molybdenum ores. This silvery gray, crystalline transition metal lies between manganese and rhenium in group 7 of the periodic table, and its chemical properties are intermediate between those of both adjacent elements.")

        ,'Ruthenium':("Ruthenium is a chemical element with the symbol Ru and atomic number 44. It is a rare transition metal belonging to the platinum group of the periodic table. Like the other metals of the platinum group, ruthenium is inert to most other chemicals. Russian-born scientist of Baltic-German ancestry Karl Ernst Claus discovered the element in 1844 at Kazan State University and named ruthenium in honor of Russia.")

        ,'Rhodium':("Rhodium is a chemical element with the symbol Rh and atomic number 45. It is a very rare, silvery-white, hard, corrosion-resistant transition metal. It is a noble metal and a member of the platinum group. It has only one naturally occurring isotope: 103Rh. Naturally occurring rhodium is usually found as a free metal or as an alloy with similar metals and rarely as a chemical compound in minerals such as bowieite and rhodplumsite. It is one of the rarest and most valuable precious metals.")

        ,'Palladium':("Palladium is a chemical element with the symbol Pd and atomic number 46. It is a rare and lustrous silvery-white metal discovered in 1803 by the English chemist William Hyde Wollaston. He named it after the asteroid Pallas, which was itself named after the epithet of the Greek goddess Athena, acquired by her when she slew Pallas. Palladium, platinum, rhodium, ruthenium, iridium and osmium form a group of elements referred to as the platinum group metals. They have similar chemical properties, but palladium has the lowest melting point and is the least dense of them")

        ,'Silver':("Silver is a chemical element with the symbol Ag and atomic number 47. A soft, white, lustrous transition metal, it exhibits the highest electrical conductivity, thermal conductivity, and reflectivity of any metal.[5] The metal is found in the Earth's crust in the pure, free elemental form ('native silver'), as an alloy with gold and other metals, and in minerals such as argentite and chlorargyrite. Most silver is produced as a byproduct of copper, gold, lead, and zinc refining.")

        ,'Cadmium':("Cadmium is a chemical element with the symbol Cd and atomic number 48. This soft, silvery-white metal is chemically similar to the two other stable metals in group 12, zinc and mercury. Like zinc, it demonstrates oxidation state +2 in most of its compounds, and like mercury, it has a lower melting point than the transition metals in groups 3 through 11. Cadmium and its congeners in group 12 are often not considered transition metals, in that they do not have partly filled d or f electron shells in the elemental or common oxidation states.")

        ,'Indium':("Indium is a chemical element with the symbol In and atomic number 49. Indium is the softest metal that is not an alkali metal. It is a silvery-white metal that resembles tin in appearance. It is a post-transition metal that makes up 0.21 parts per million of the Earth's crust. Indium has a melting point higher than sodium and gallium, but lower than lithium and tin. Chemically, indium is similar to gallium and thallium, and it is largely intermediate between the two in terms of its properties.")

        ,'Tin':("Tin is a chemical element with the symbol Sn and atomic number 50. Tin is a silvery-coloured metal.Tin is soft enough to be cut with little force and a bar of tin can be bent by hand with little effort. When bent, the so-called 'tin cry' can be heard as a result of twinning in tin crystals; this trait is shared by indium, cadmium, zinc, and mercury in the solid state.")

        ,'Antimony':("Antimony is a chemical element with the symbol Sb and atomic number 51. A lustrous gray metalloid, it is found in nature mainly as the sulfide mineral stibnite.")

        ,'Tellurium':("Tellurium is a chemical element with the symbol Te and atomic number 52. It is a brittle, mildly toxic, rare, silver-white metalloid. Tellurium is chemically related to selenium and sulfur, all three of which are chalcogens. It is occasionally found in native form as elemental crystals. Tellurium is far more common in the Universe as a whole than on Earth. Its extreme rarity in the Earth's crust, comparable to that of platinum, is due partly to its formation of a volatile hydride that caused tellurium to be lost to space as a gas during the hot nebular formation of Earth.")

        ,'Iodine':("Iodine is a chemical element with the symbol I and atomic number 53. The heaviest of the stable halogens, it exists as a semi-lustrous, non-metallic solid at standard conditions that melts to form a deep violet liquid at 114 °C (237 °F), and boils to a violet gas at 184 °C (363 °F). The element was discovered by the French chemist Bernard Courtois in 1811 and was named two years later by Joseph Louis Gay-Lussac")

        ,'Xenon':("Xenon is a chemical element with the symbol Xe and atomic number 54. It is a dense, colorless, odorless noble gas found in Earth's atmosphere in trace amounts. Although generally unreactive, it can undergo a few chemical reactions such as the formation of xenon hexafluoroplatinate, the first noble gas compound to be synthesized.")

        ,'Caesium':("Caesium is a chemical element with the symbol Cs and atomic number 55. It is a soft, silvery-golden alkali metal with a melting point of 28.5 °C (83.3 °F), which makes it one of only five elemental metals that are liquid at or near room temperature.Caesium has physical and chemical properties similar to those of rubidium and potassium. It is pyrophoric and reacts with water even at −116 °C (−177 °F).")

        ,'Barium':("Barium is a chemical element with the symbol Ba and atomic number 56. It is the fifth element in group 2 and is a soft, silvery alkaline earth metal. Because of its high chemical reactivity, barium is never found in nature as a free element.")

        ,'Lanthanum':("Lanthanum is a chemical element with the symbol La and atomic number 57. It is a soft, ductile, silvery-white metal that tarnishes slowly when exposed to air. It is the eponym of the lanthanide series, a group of 15 similar elements between lanthanum and lutetium in the periodic table, of which lanthanum is the first and the prototype. Lanthanum is traditionally counted among the rare earth elements. Like most other rare earth elements, the usual oxidation state is +3.")

        ,'Cerium':("Cerium is a chemical element with the symbol Ce and atomic number 58. Cerium is a soft, ductile, and silvery-white metal that tarnishes when exposed to air. Cerium is the second element in the lanthanide series, and while it often shows the +3 oxidation state characteristic of the series, it also has a stable +4 state that does not oxidize water. It is also considered one of the rare-earth elements. Cerium has no known biological role in humans but is not particularly toxic, except with intense or continued exposure.")

        ,'Praseodymium':("Praseodymium is a chemical element with the symbol Pr and the atomic number 59. It is the third member of the lanthanide series and is considered to be one of the rare-earth metals. It is a soft, silvery, malleable and ductile metal, valued for its magnetic, electrical, chemical, and optical properties. It is too reactive to be found in native form, and pure praseodymium metal slowly develops a green oxide coating when exposed to air.")

        ,'Neodymium':("Neodymium is a chemical element with the symbol Nd and atomic number 60. It is the fourth member of the lanthanide series and is considered to be one of the rare-earth metals. It is a hard, slightly malleable, silvery metal that quickly tarnishes in air and moisture. When oxidized, neodymium reacts quickly producing pink, purple/blue and yellow compounds in the +2, +3 and +4 oxidation states.")

        ,'Promethium':("Promethium is a chemical element with the symbol Pm and atomic number 61. All of its isotopes are radioactive; it is extremely rare, with only about 500–600 grams naturally occurring in Earth's crust at any given time. Promethium is one of only two radioactive elements that are followed in the periodic table by elements with stable forms, the other being technetium. Chemically, promethium is a lanthanide.")

        ,'Samarium':("Samarium is a chemical element with symbol Sm and atomic number 62. It is a moderately hard silvery metal that slowly oxidizes in air. Being a typical member of the lanthanide series, samarium usually has the oxidation state +3. Compounds of samarium(II) are also known, most notably the monoxide SmO, monochalcogenides SmS, SmSe and SmTe, as well as samarium(II) iodide.")

        ,'Europium':("Europium is a chemical element with the symbol Eu and atomic number 63. Europium is the most reactive lanthanide by far, having to be stored under an inert fluid to protect it from atmospheric oxygen or moisture. Europium is also the softest lanthanide, as it can be dented with a fingernail and easily cut with a knife. When oxidation is removed a shiny-white metal is visible. Europium was isolated in 1901 and is named after the continent of Europe.")

        ,'Gadolinium':("Gadolinium is a chemical element with the symbol Gd and atomic number 64. Gadolinium is a silvery-white metal when oxidation is removed. It is only slightly malleable and is a ductile rare-earth element. Gadolinium reacts with atmospheric oxygen or moisture slowly to form a black coating. Gadolinium below its Curie point of 20 °C (68 °F) is ferromagnetic, with an attraction to a magnetic field higher than that of nickel. Above this temperature it is the most paramagnetic element.")

        ,'Terbium':("Terbium is a chemical element with the symbol Tb and atomic number 65. It is a silvery-white, rare earth metal that is malleable, and ductile. The ninth member of the lanthanide series, terbium is a fairly electropositive metal that reacts with water, evolving hydrogen gas. Terbium is never found in nature as a free element, but it is contained in many minerals, including cerite, gadolinite, monazite, xenotime and euxenite.")

        ,'Dysprosium':("Dysprosium is the chemical element with the symbol Dy and atomic number 66. It is a rare-earth element in the lanthanide series with a metallic silver luster. Dysprosium is never found in nature as a free element, though, like other lanthanides, it is found in various minerals, such as xenotime.")

        ,'Holmium':("Holmium is a chemical element with the symbol Ho and atomic number 67. It is a rare-earth element and the eleventh member of the lanthanide series. It is a relatively soft, silvery, fairly corrosion-resistant and malleable metal. Like a lot of other lanthanides, holmium is too reactive to be found in native form, as pure holmium slowly forms a yellowish oxide coating when exposed to air.")

        ,'Erbium':("Erbium is a chemical element with the symbol Er and atomic number 68. A silvery-white solid metal when artificially isolated, natural erbium is always found in chemical combination with other elements. It is a lanthanide, a rare-earth element, originally found in the gadolinite mine in Ytterby, Sweden, which is the source of the element's name.")

        ,'Thulium':("Thulium is a chemical element with the symbol Tm and atomic number 69. It is the thirteenth and third-last element in the lanthanide series. Like the other lanthanides, the most common oxidation state is +3, seen in its oxide, halides and other compounds; however, the +2 oxidation state can also be stable. In aqueous solution, like compounds of other late lanthanides, soluble thulium compounds form coordination complexes with nine water molecules.")

        ,'Ytterbium':("Ytterbium is a chemical element with the symbol Yb and atomic number 70. It is a metal, the fourteenth and penultimate element in the lanthanide series, which is the basis of the relative stability of its +2 oxidation state. However, like the other lanthanides, its most common oxidation state is +3, as in its oxide, halides, and other compounds. In aqueous solution, like compounds of other late lanthanides, soluble ytterbium compounds form complexes with nine water molecules. Because of its closed-shell electron configuration, its density and melting and boiling points differ significantly from those of most other lanthanides.")

        ,'Lutetium':("Lutetium is a chemical element with the symbol Lu and atomic number 71. It is a silvery white metal, which resists corrosion in dry air, but not in moist air. Lutetium is the last element in the lanthanide series, and it is traditionally counted among the rare earths. Lutetium is generally considered the first element of the 6th-period transition metals by those who study the matter, although there has been some dispute on this point.")

        ,'Hafnium':("Hafnium is a chemical element with the symbol Hf and atomic number 72. A lustrous, silvery gray, tetravalent transition metal, hafnium chemically resembles zirconium and is found in many zirconium minerals. Its existence was predicted by Dmitri Mendeleev in 1869, though it was not identified until 1923, by Dirk Coster and George de Hevesy")

        ,'Tantalum':("Tantalum is a chemical element with the symbol Ta and atomic number 73. Previously known as tantalium, it is named after Tantalus, a villain in Greek mythology. Tantalum is a very hard, ductile, lustrous, blue-gray transition metal that is highly corrosion-resistant. It is part of the refractory metals group, which are widely used as components of strong high-melting-point alloys. It is a group 5 element, along with vanadium and niobium, and it always occurs in geologic sources together with the chemically similar niobium, mainly in the mineral groups tantalite, columbite and coltan.")

        ,'Tungsten':("Tungsten, or wolfram is a chemical element with the symbol W and atomic number 74. Tungsten is a rare metal found naturally on Earth almost exclusively as compounds with other elements. It was identified as a new element in 1781 and first isolated as a metal in 1783. Its important ores include scheelite and wolframite, the latter lending the element its alternate name.")

        ,'Rhenium':("Rhenium is a chemical element with the symbol Re and atomic number 75. It is a silvery-gray, heavy, third-row transition metal in group 7 of the periodic table. With an estimated average concentration of 1 part per billion , rhenium is one of the rarest elements in the Earth's crust. Rhenium has the third-highest melting point and highest boiling point of any stable element at 5869 K. Rhenium resembles manganese and technetium chemically and is mainly obtained as a by-product of the extraction and refinement of molybdenum and copper ores.")

        ,'Osmium':("Osmium is a chemical element with the symbol Os and atomic number 76. It is a hard, brittle, bluish-white transition metal in the platinum group that is found as a trace element in alloys, mostly in platinum ores. Osmium is the densest naturally occurring element. When experimentally measured using X-ray crystallography, it has a density of 22.59 g/cm3.")

        ,'Iridium':("Iridium is a chemical element with the symbol Ir and atomic number 77. A very hard, brittle, silvery-white transition metal of the platinum group, it is considered the second-densest naturally occurring metal with a density of 22.56 g/cm3 as defined by experimental X-ray crystallography. It is one of the most corrosion-resistant metals, even at temperatures as high as 2,000 °C (3,630 °F).")

        ,'Platinum':("Platinum is a chemical element with the symbol Pt and atomic number 78. It is a dense, malleable, ductile, highly unreactive, precious, silverish-white transition metal. Its name originates from Spanish 'platina', a diminutive of plata 'silver'.")

        ,'Gold':("Gold is a chemical element with the symbol Au and atomic number 79. This makes it one of the higher atomic number elements that occur naturally. It is a bright, slightly orange-yellow, dense, soft, malleable, and ductile metal in a pure form. Chemically, gold is a transition metal and a group 11 element. It is one of the least reactive chemical elements and is solid under standard conditions. Gold often occurs in free elemental form, as nuggets or grains, in rocks, veins, and alluvial deposits.")

        ,'Mercury':("Mercury is a chemical element with the symbol Hg and atomic number 80. It is also known as quicksilver and was formerly named hydrargyrum from the Greek words, hydor and argyros. A heavy, silvery d-block element, mercury is the only metallic element that is known to be liquid at standard conditions for temperature and pressure; the only other element that is liquid under these conditions is the halogen bromine, though metals such as caesium, gallium, and rubidium melt just above room temperature.")

        ,'Thallium':("Thallium is a chemical element with the symbol Tl and atomic number 81. It is a gray post-transition metal that is not found free in nature. When isolated, thallium resembles tin, but discolors when exposed to air. Chemists William Crookes and Claude-Auguste Lamy discovered thallium independently in 1861, in residues of sulfuric acid production. Both used the newly developed method of flame spectroscopy, in which thallium produces a notable green spectral line.")

        ,'Lead':("Lead is a chemical element with the symbol Pb and atomic number 82. It is a heavy metal that is denser than most common materials. Lead is soft and malleable, and also has a relatively low melting point. When freshly cut, lead is a shiny gray with a hint of blue. It tarnishes to a dull gray color when exposed to air. Lead has the highest atomic number of any stable element and three of its isotopes are endpoints of major nuclear decay chains of heavier elements. Lead is toxic, even in small amounts, especially to children.")

        ,'Bismuth':("Bismuth is a chemical element with the symbol Bi and atomic number 83. It is a post-transition metal and one of the pnictogens, with chemical properties resembling its lighter group 15 siblings arsenic and antimony. Elemental bismuth occurs naturally, and its sulfide and oxide forms are important commercial ores. The free element is 86% as dense as lead. It is a brittle metal with a silvery-white color when freshly produced. Surface oxidation generally gives samples of the metal a somewhat rosy cast.")

        ,'Polonium':("Polonium is a chemical element with the symbol Po and atomic number 84. Polonium is a chalcogen. A rare and highly radioactive metal with no stable isotopes, polonium is chemically similar to selenium and tellurium, though its metallic character resembles that of its horizontal neighbors in the periodic table: thallium, lead, and bismuth. Due to the short half-life of all its isotopes, its natural occurrence is limited to tiny traces of the fleeting polonium-210 (with a half-life of 138 days) in uranium ores, as it is the penultimate daughter of natural uranium-238.")

        ,'Astatine':("Astatine is a chemical element with the symbol At and atomic number 85. It is the rarest naturally occurring element in the Earth's crust, occurring only as the decay product of various heavier elements. All of astatine's isotopes are short-lived; the most stable is astatine-210, with a half-life of 8.1 hours. A sample of the pure element has never been assembled, because any macroscopic specimen would be immediately vaporized by the heat of its own radioactivity.")

        ,'Radon':("Radon is a chemical element with the symbol Rn and atomic number 86. It is a radioactive, colourless, odourless, tasteless noble gas. It occurs naturally in minute quantities as an intermediate step in the normal radioactive decay chains through which thorium and uranium slowly decay into various short-lived radioactive elements and lead. Radon itself is the immediate decay product of radium.")

        ,'Francium':("Francium is a chemical element with the symbol Fr and atomic number 87. It is extremely radioactive; its most stable isotope, francium-223 , has a half-life of only 22 minutes. It is the second-most electropositive element, behind only caesium, and is the second rarest naturally occurring element.")

        ,'Radium':("Radium is a chemical element with the symbol Ra and atomic number 88. It is the sixth element in group 2 of the periodic table, also known as the alkaline earth metals. Pure radium is silvery-white, but it readily reacts with nitrogen upon exposure to air, forming a black surface layer of radium nitride ")

        ,'Actinium':("Actinium is a chemical element with the symbol Ac and atomic number 89. It was first isolated by Friedrich Oskar Giesel in 1902, who gave it the name emanium; the element got its name by being wrongly identified with a substance André-Louis Debierne found in 1899 and called actinium. Actinium gave the name to the actinide series, a group of 15 similar elements between actinium and lawrencium in the periodic table.")

        ,'Thorium':("Thorium is a weakly radioactive metallic chemical element with the symbol Th and atomic number 90. Thorium is silvery and tarnishes black when it is exposed to air, forming thorium dioxide; it is moderately soft and malleable and has a high melting point. Thorium is an electropositive actinide whose chemistry is dominated by the +4 oxidation state; it is quite reactive and can ignite in air when finely divided.")

        ,'Protactinium':("Protactinium is a chemical element with the symbol Pa and atomic number 91. It is a dense, silvery-gray actinide metal which readily reacts with oxygen, water vapor and inorganic acids. It forms various chemical compounds in which protactinium is usually present in the oxidation state +5, but it can also assume +4 and even +3 or +2 states. Concentrations of protactinium in the Earth's crust are typically a few parts per trillion, but may reach up to a few parts per million in some uraninite ore deposits.")

        ,'Uranium':("Uranium is a chemical element with the symbol U and atomic number 92. It is a silvery-grey metal in the actinide series of the periodic table. A uranium atom has 92 protons and 92 electrons, of which 6 are valence electrons. Uranium is weakly radioactive because all isotopes of uranium are unstable; the half-lives of its naturally occurring isotopes range between 159,200 years and 4.5 billion years.")

        ,'Neptunium':("Neptunium is a chemical element with the symbol Np and atomic number 93. A radioactive actinide metal, neptunium is the first transuranic element. Its position in the periodic table just after uranium, named after the planet Uranus, led to it being named after Neptune, the next planet beyond Uranus. A neptunium atom has 93 protons and 93 electrons, of which seven are valence electrons. Neptunium metal is silvery and tarnishes when exposed to air.")

        ,'Plutonium':("Plutonium is a radioactive chemical element with the symbol Pu and atomic number 94. It is an actinide metal of silvery-gray appearance that tarnishes when exposed to air, and forms a dull coating when oxidized. The element normally exhibits six allotropes and four oxidation states. It reacts with carbon, halogens, nitrogen, silicon, and hydrogen. When exposed to moist air, it forms oxides and hydrides that can expand the sample up to 70% in volume, which in turn flake off as a powder that is pyrophoric. It is radioactive and can accumulate in bones, which makes the handling of plutonium dangerous.")

        ,'Americium':("Americium is a synthetic radioactive chemical element with the symbol Am and atomic number 95. It is a transuranic member of the actinide series, in the periodic table located under the lanthanide element europium, and thus by analogy was named after the Americas.")

        ,'Curium':("Curium is a transuranic, radioactive chemical element with the symbol Cm and atomic number 96. This actinide element was named after eminent scientists Marie and Pierre Curie, both known for their research on radioactivity. Curium was first intentionally made by the team of Glenn T. Seaborg, Ralph A. James, and Albert Ghiorso in 1944, using the cyclotron at Berkeley.")

        ,'Berkelium':("Berkelium is a transuranic radioactive chemical element with the symbol Bk and atomic number 97. It is a member of the actinide and transuranium element series. It is named after the city of Berkeley, California, the location of the Lawrence Berkeley National Laboratory where it was discovered in December 1949. Berkelium was the fifth transuranium element discovered after neptunium, plutonium, curium and americium.")

        ,'Californium':("Californium is a radioactive chemical element with the symbol Cf and atomic number 98. The element was first synthesized in 1950 at Lawrence Berkeley National Laboratory , by bombarding curium with alpha particles . It is an actinide element, the sixth transuranium element to be synthesized, and has the second-highest atomic mass of all elements that have been produced in amounts large enough to see with the naked eye.")

        ,'Einsteinium':("Einsteinium is a synthetic element with the symbol Es and atomic number 99. Einsteinium is a member of the actinide series and it is the seventh transuranium element. It was named in honor of Albert Einstein.Einsteinium was discovered as a component of the debris of the first hydrogen bomb explosion in 1952. Its most common isotope, einsteinium-253, is produced artificially from decay of californium-253 in a few dedicated high-power nuclear reactors with a total yield on the order of one milligram per year.")

        ,'Fermium':("Fermium is a synthetic element with the symbol Fm and atomic number 100. It is an actinide and the heaviest element that can be formed by neutron bombardment of lighter elements, and hence the last element that can be prepared in macroscopic quantities, although pure fermium metal has not yet been prepared.")

        ,'Mendelevium':("Mendelevium is a synthetic element with the symbol Md (formerly Mv) and atomic number 101. A metallic radioactive transuranium element in the actinide series, it is the first element by atomic number that currently cannot be produced in macroscopic quantities by neutron bombardment of lighter elements. It is the third-to-last actinide and the ninth transuranic element. It can only be produced in particle accelerators by bombarding lighter elements with charged particles.")

        ,'Nobelium':("Nobelium is a synthetic chemical element with the symbol No and atomic number 102. It is named in honor of Alfred Nobel, the inventor of dynamite and benefactor of science. A radioactive metal, it is the tenth transuranic element and is the penultimate member of the actinide series. Like all elements with atomic number over 100, nobelium can only be produced in particle accelerators by bombarding lighter elements with charged particles.")

        ,'Lawrencium':("Lawrencium is a synthetic chemical element with the symbol Lr and atomic number 103. It is named in honor of Ernest Lawrence, inventor of the cyclotron, a device that was used to discover many artificial radioactive elements. A radioactive metal, lawrencium is the eleventh transuranic element and the last member of the actinide series.")

        ,'Rutherfordium':("Rutherfordium is a chemical element with the symbol Rf and atomic number 104, named after New Zealand-born British physicist Ernest Rutherford. As a synthetic element, it is not found in nature and can only be made in a laboratory. It is radioactive; the most stable known isotope, 267Rf, has a half-life of ~1.3 hours.")

        ,'Dubnium':("Dubnium is a synthetic chemical element with the symbol Db and atomic number 105. It is highly radioactive: the most stable known isotope, dubnium-268, has a half-life of about 28 hours. This greatly limits extended research on the element.")

        ,'Seaborgium':("Seaborgium is a synthetic chemical element with the symbol Sg and atomic number 106. It is named after the American nuclear chemist Glenn T. Seaborg. As a synthetic element, it can be created in a laboratory but is not found in nature. It is also radioactive; the most stable known isotope, 269Sg, has a half-life of approximately 14 minutes.")

        ,'Bohrium':("Bohrium is a synthetic chemical element with the symbol Bh and atomic number 107. It is named after Danish physicist Niels Bohr. As a synthetic element, it can be created in a laboratory but is not found in nature. All known isotopes of bohrium are highly radioactive; the most stable known isotope is 270Bh with a half-life of approximately 61 seconds, though the unconfirmed 278Bh may have a longer half-life of about 690 seconds.")

        ,'Hassium':("Hassium is a chemical element with the symbol Hs and the atomic number 108. Hassium is highly radioactive; its most stable known isotopes have half-lives of approximately ten seconds. One of its isotopes, 270Hs, has magic numbers of both protons and neutrons for deformed nuclei, which gives it greater stability against spontaneous fission. Hassium is a superheavy element; it has been produced in a laboratory only in very small quantities by fusing heavy nuclei with lighter ones. Natural occurrences of the element have been hypothesised but never found.")

        ,'Meitnerium':("Meitnerium is a synthetic chemical element with the symbol Mt and atomic number 109. It is an extremely radioactive synthetic element. The most stable known isotope, meitnerium-278, has a half-life of 4.5 seconds, although the unconfirmed meitnerium-282 may have a longer half-life of 67 seconds. The GSI Helmholtz Centre for Heavy Ion Research near Darmstadt, Germany, first created this element in 1982. It is named after Lise Meitner.")

        ,'Darmstadtium':("Darmstadtium is a chemical element with the symbol Ds and atomic number 110. It is an extremely radioactive synthetic element. The most stable known isotope, darmstadtium-281, has a half-life of approximately 12.7 seconds. Darmstadtium was first created in 1994 by the GSI Helmholtz Centre for Heavy Ion Research in the city of Darmstadt, Germany, after which it was named.")

        ,'Roentgenium':("Roentgenium is a chemical element with the symbol Rg and atomic number 111. It is an extremely radioactive synthetic element that can be created in a laboratory but is not found in nature. The most stable known isotope, roentgenium-282, has a half-life of 100 seconds, although the unconfirmed roentgenium-286 may have a longer half-life of about 10.7 minutes.")

        ,'Copernicium':("Copernicium is a synthetic chemical element with the symbol Cn and atomic number 112. Its known isotopes are extremely radioactive, and have only been created in a laboratory. The most stable known isotope, copernicium-285, has a half-life of approximately 28 seconds. Copernicium was first created in 1996 by the GSI Helmholtz Centre for Heavy Ion Research ")

        ,'Nihonium':("Nihonium is a synthetic chemical element with the symbol Nh and atomic number 113. It is extremely radioactive; its most stable known isotope, nihonium-286, has a half-life of about 10 seconds. In the periodic table, nihonium is a transactinide element in the p-block. It is a member of period 7 and group 13 ")

        ,'Flerovium':("Flerovium is a superheavy chemical element with symbol Fl and atomic number 114. It is an extremely radioactive synthetic element. It is named after the Flerov Laboratory of Nuclear Reactions of the Joint Institute for Nuclear Research in Dubna, Russia, where the element was discovered in 1998. The lab's name, in turn, honours Russian physicist Georgy Flyorov. IUPAC adopted the name on 30 May 2012. The name and symbol had previously been proposed for element 102 , but was not accepted by IUPAC at that time.")

        ,'Moscovium':("Moscovium is a synthetic element with the symbol Mc and atomic number 115. It was first synthesized in 2003 by a joint team of Russian and American scientists at the Joint Institute for Nuclear Research in Dubna, Russia. In December 2015, it was recognized as one of four new elements by the Joint Working Party of international scientific bodies IUPAC and IUPAP. On 28 November 2016, it was officially named after the Moscow Oblast, in which the JINR is situated.")

        ,'Livermorium':("Livermorium is a synthetic chemical element with the symbol Lv and has an atomic number of 116. It is an extremely radioactive element that has only been created in a laboratory setting and has not been observed in nature. The element is named after the Lawrence Livermore National Laboratory in the United States, which collaborated with the Joint Institute for Nuclear Research in Dubna, Russia to discover livermorium during experiments conducted between 2000 and 2006. The name of the laboratory refers to the city of Livermore, California where it is located, which in turn was named after the rancher and landowner Robert Livermore.")

        ,'Tennessine':("Tennessine is a synthetic chemical element with the symbol Ts and atomic number 117. It is the second-heaviest known element and the penultimate element of the 7th period of the periodic table.")

        ,'Oganesson':("Oganesson is a synthetic chemical element with the symbol Og and atomic number 118. It was first synthesized in 2002 at the Joint Institute for Nuclear Research in Dubna, near Moscow, Russia, by a joint team of Russian and American scientists. In December 2015, it was recognized as one of four new elements by the Joint Working Party of the international scientific bodies IUPAC and IUPAP.")}



    a=str(input("Enter the name of the element you want to get info about:"))

    print("------------------------------------------------------------------------------------------------------------------")

    print(d1[a])

    print("------------------------------------------------------------------------------------------------------------------")

    print()

    time.sleep(3)

    print("Do you want to search for another element(Y/N):")

    d=input("Enter your choice:")


    if d=="y":

        i=i-1

    if d=="n":

        i=i+10


        
        
    
