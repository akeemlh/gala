""" This module contains dictionaries that can be used to set a
matplotlib plotting style.
It is mostly here to allow a consistent plotting style in tutorials,
but can be used to prepare any matplotlib figure.

Using a matplotlib version > 1.4 you can do::

    >>> import matplotlib.pyplot as pl
    >>> from gala.mpl_style import mpl_style
    >>> pl.style.use(mpl_style) # doctest: +SKIP

for older versions of matplotlib the following works::

    >>> import matplotlib as mpl
    >>> from gala.mpl_style import mpl_style
    >>> mpl.rcParams.update(mpl_style) # doctest: +SKIP

"""
try:
    import matplotlib
    from matplotlib.colors import ListedColormap
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

# custom colormaps from http://inversed.ru/Blog_2.htm#Proposed
_hesperia_data = [(0,0,0),
    (0.008680399042477699,0.00013116305198120114,0.0499894378955346),
    (0.015688806352492674,0.0004574270049853096,0.08685339309628601),
    (0.02150865143471113,0.0009088537966835834,0.11462751931896643),
    (0.02675031888909726,0.0014581050791102894,0.1374228438792915),
    (0.03166556852694796,0.0020899683026478918,0.15700249688184162),
    (0.03638092804239181,0.0027944474768103393,0.17429344774222616),
    (0.040967078162138744,0.0035642300000921726,0.18984371091880567),
    (0.0454411490323747,0.00439114046932907,0.20389222785736105),
    (0.049829398712932876,0.0052697277775547845,0.21668874803099905),
    (0.054157581311500246,0.006196313107564053,0.22845144685412125),
    (0.058441862768924435,0.00716761290864468,0.23933418544650703),
    (0.06269445963059038,0.008180898667775494,0.24945795516171806),
    (0.06692365518230464,0.009233717922975148,0.2589154033310103),
    (0.07113621239146699,0.010324004316796616,0.267783675936872),
    (0.07533576536240061,0.01144970883261157,0.2761205144560239),
    (0.07952640218216642,0.012609207925501872,0.2839795055702526),
    (0.08371025536226033,0.013800879938102409,0.2914021862340312),
    (0.08788895747231389,0.01502325860127822,0.2984244403658532),
    (0.09206365647747364,0.016274994560059198,0.3050772092072735),
    (0.09623508889197716,0.01755483314144379,0.31138729266998494),
    (0.1004192611214301,0.018864530956222283,0.317427381326767),
    (0.10467993738263243,0.020215516486748412,0.3234112261116334),
    (0.10902331953352103,0.021609191211184337,0.3293597816052254),
    (0.11344853922670949,0.023045657293481195,0.33527126857060896),
    (0.11795471116867644,0.024525004610279955,0.34114398757419084),
    (0.12254092665985504,0.026047309714654132,0.34697629316095996),
    (0.12720621910862073,0.027612628487918338,0.3527664934616959),
    (0.13194962519826262,0.029221009032246514,0.35851302187184614),
    (0.13677014710681917,0.030872483825306468,0.3642143248116954),
    (0.14166676429606695,0.03256707225196946,0.3698688920045103),
    (0.14663843521710382,0.034304781057000557,0.3754752574560281),
    (0.1516840991637631,0.036085604849644376,0.3810320006851322),
    (0.15680267802700615,0.03790952660377405,0.3865377475621281),
    (0.1619930780252838,0.039776518168584594,0.39199117098395453),
    (0.16724460913120412,0.04168415249523942,0.39736822419293905),
    (0.1725469002727291,0.043629937548758366,0.4026473071793794),
    (0.1779006044356746,0.045614074207531684,0.40783360751479236),
    (0.1833039710447741,0.04763616464809869,0.41292654094596776),
    (0.18875525591293624,0.04969580432498367,0.41792557866850505),
    (0.19425272354511786,0.05179258279083796,0.4228302484209565),
    (0.19979464934948563,0.053926084515430815,0.42764013524100897),
    (0.2053793215021562,0.05609588963156172,0.432354881385471),
    (0.21100504294527664,0.05830157473242858,0.43697418650008024),
    (0.21667013326129836,0.06054271365162168,0.4414978074853968),
    (0.22237293030158245,0.06281887818864339,0.4459255578461445),
    (0.22811179175165416,0.06512963882694765,0.4502573069389346),
    (0.23388509657872614,0.06747456542786946,0.4544929790227298),
    (0.2396912463622177,0.06985322789865403,0.4586325521337542),
    (0.2455286665085125,0.07226519683307527,0.4626760568052306),
    (0.25139580735167055,0.07471004412339613,0.4666235746510806),
    (0.2572911451422554,0.0771873435426767,0.4704752368315531),
    (0.2632131829268324,0.0796966712966696,0.47423122241762167),
    (0.2691604513210541,0.08223760654476461,0.47789175666991596),
    (0.27513150917956947,0.08480973188965069,0.4814571092469274),
    (0.2811249441662692,0.08741263383555446,0.484927592356226),
    (0.2871393732286182,0.09004590321509086,0.4883035588614687),
    (0.2931734429800271,0.09270913558492197,0.4915854003570529),
    (0.2992258299943774,0.09540193159056867,0.49477354522137057),
    (0.30529524101693706,0.09812389730084943,0.4978684566587513),
    (0.31138041309600184,0.1008746445125406,0.5008706307393509),
    (0.3174801136396537,0.10365379102595644,0.5037805944454394),
    (0.3235931404020573,0.10646096089223722,0.5065989037317653),
    (0.32971832140372387,0.10929578463321525,0.5093261416069421),
    (0.3358545147901406,0.11215789943479176,0.5119629162420862),
    (0.3420005110691422,0.11504691649487847,0.5145097123358336),
    (0.3481554299168305,0.11796255451425826,0.5169674884049023),
    (0.3543181138594905,0.12090443665029683,0.5193367576952266),
    (0.36048753903779346,0.12387222817942976,0.5216182108493176),
    (0.3666627102375976,0.12686560164830935,0.5238125547994394),
    (0.37284266046715603,0.12988423693023182,0.5259205111349294),
    (0.3790264505012281,0.13292782126262348,0.5279428145234838),
    (0.3852131683956696,0.13599604926670322,0.5298802111881918),
    (0.3914019289759207,0.1390886229504287,0.531733457441692),
    (0.39759187330265655,0.1422052516958178,0.5335033182784523),
    (0.4037821681177014,0.14534565223171708,0.5351905660258294),
    (0.40997200527314814,0.14850954859306428,0.5367959790542475),
    (0.4161606011464567,0.15169667206766527,0.5383203405465532),
    (0.42234719604414467,0.1549067611314736,0.5397644373263348),
    (0.4285310535965201,0.1581395613733306,0.5411290587447741),
    (0.43471146014574974,0.16139482541008754,0.5424149956253794),
    (0.44088772412939287,0.16467231279299493,0.5436230392657636),
    (0.4470591754613845,0.16797178990620806,0.5447539804954755),
    (0.45322516491230175,0.1712930298582188,0.5458086087887438),
    (0.45938506349059904,0.17463581236698522,0.5467877114308693),
    (0.46553826182636765,0.1779999236394936,0.5476920727369035),
    (0.47168416955903497,0.181385156246446,0.5485224733211577),
    (0.477822214730295,0.18479130899273183,0.5492796894160185),
    (0.4839518431834482,0.18821818678430405,0.5499644922384906),
    (0.4900725176129956,0.19166560035234098,0.5505776470015353),
    (0.4961837181068953,0.19513336655399613,0.5511199136457458),
    (0.5022849405077602,0.19862130781974846,0.551592045122552),
    (0.5083756959505333,0.20212925204921545,0.5519947870661353),
    (0.5144555105551393,0.20565703256498646,0.5523288776512739),
    (0.5205239269568815,0.20920448880315046,0.552595049409582),
    (0.5265804944429084,0.21277146242176273,0.5527940189612377),
    (0.5326246634820281,0.21635775444770733,0.5529263781760881),
    (0.5386564541063357,0.21996339707521725,0.552993287027223),
    (0.5446751630749685,0.2235881289865154,0.5529951295044349),
    (0.5506798473856149,0.22723158704222388,0.5529320411965789),
    (0.556670950964606,0.2308939783650991,0.5528055383803692),
    (0.5626477968255406,0.2345750495429707,0.5526159794958311),
    (0.5686100225071714,0.23827467609824332,0.5523640218641095),
    (0.5745572002510438,0.2419927058072243,0.5520502404859028),
    (0.580489168620069,0.24572909831795475,0.5516754474436031),
    (0.5864073492859379,0.2494844881483934,0.551241916670736),
    (0.5923057118938185,0.25325633827866745,0.5507449030709336),
    (0.5981897094748121,0.2570469973839509,0.5501904368455359),
    (0.604057144101911,0.26085555918211745,0.5495773372307642),
    (0.6099077045750838,0.2646819199235265,0.5489061800232677),
    (0.6157410874861254,0.26852597903526154,0.5481775316186452),
    (0.6215569749781713,0.2723876294052942,0.547391929707449),
    (0.6273550689042748,0.27626677221986284,0.5465499143561524),
    (0.633135135733615,0.2801633369952615,0.5456520663790427),
    (0.6388969043117971,0.28407723676008845,0.5446989177698661),
    (0.6446401136010722,0.28800838893643665,0.5436909943224516),
    (0.6503645081432644,0.2919567133662193,0.5426288119553462),
    (0.6560698377975348,0.2959221322088912,0.541512876800358),
    (0.6617558574884893,0.29990456984183306,0.5403436852988648),
    (0.6674223269643506,0.3039039527633791,0.5391217243051842),
    (0.6730690105649308,0.3079202094984786,0.5378474711963558),
    (0.6786956769991164,0.31195327050695815,0.5365213939877027),
    (0.6843021010905821,0.3160030689990033,0.5351439529855792),
    (0.6898879545121279,0.3200694902712787,0.5337155164577343),
    (0.695452914049575,0.3241524210202781,0.5322364482235586),
    (0.7009978587202182,0.32825230992747023,0.5307080140940897),
    (0.7065209347947679,0.3323683295073232,0.5291293862051887),
    (0.7120228599767251,0.33650085322632317,0.5275016842014247),
    (0.717503254495308,0.34064974145347754,0.5258251827632342),
    (0.7229619150512071,0.34481493712650835,0.5241002796861228),
    (0.7283986410952034,0.3489963844042398,0.5223273646183857),
    (0.7338132346861131,0.35319402859899396,0.5205068192074948),
    (0.7392055003553802,0.3574078161111607,0.5186390172474807),
    (0.7445752449780715,0.3616376943658896,0.5167243248270206),
    (0.7499222776500555,0.36588361175186235,0.5147631004779718),
    (0.7552464095711345,0.37014551756209074,0.5127556953241085),
    (0.7605475402946779,0.3744234044527645,0.5107025112204987),
    (0.765825295564327,0.3787171302985865,0.5086037572688031),
    (0.7710795975464707,0.38302669839236636,0.5064598346956509),
    (0.7763103182683837,0.3873520877856565,0.5042711011546184),
    (0.7815172809433065,0.3916932533761069,0.5020378737083536),
    (0.7867001908580512,0.3960500905484942,0.499760386951951),
    (0.7918589172435819,0.40042257636524115,0.4974389745006173),
    (0.7969932803478447,0.4048106632299109,0.4950739311501965),
    (0.8021031018536915,0.4092143040384373,0.4926655458091624),
    (0.8071879266013618,0.4136333095742001,0.49021393267281266),
    (0.8122481998806693,0.41806795130655233,0.48771974784169436),
    (0.8172832835069203,0.4225179459431898,0.48518298099808727),
    (0.822293470294766,0.4269834891306363,0.4826041748040191),
    (0.8272781113252743,0.43146428933361575,0.4799833071092487),
    (0.8322372034529658,0.43596038864561015,0.4773207332094245),
    (0.8371705893745123,0.44047174928970356,0.47461671096005925),
    (0.8420780875353928,0.4449983204814673,0.47187147889117875),
    (0.846959564431738,0.4495400765060763,0.4690852972237319),
    (0.8518148296668729,0.45409696131286614,0.46625838903625),
    (0.8566437220961142,0.4586689339607668,0.4633909888745702),
    (0.8614460782532785,0.4632559519618739,0.46048332509083045),
    (0.8662217399730128,0.4678579753540265,0.4575356241019586),
    (0.8709705443821578,0.4724749613167537,0.45454810515194466),
    (0.8756925231543607,0.4771069726597484,0.45152108334864666),
    (0.8803869311632703,0.4817536485866979,0.4484544689571619),
    (0.8850541950198868,0.4864152663389204,0.445348772155453),
    (0.8892746166580348,0.49133150637033585,0.4425247713197049),
    (0.8921242547544529,0.49701914159743477,0.44074379122442114),
    (0.894933339156845,0.5027090015197095,0.4390219334399727),
    (0.8977019408608369,0.5084009935812441,0.4373606747346031),
    (0.9004301709891707,0.5140952119116522,0.4357617506739443),
    (0.9031181978033653,0.5197920361730285,0.43422728953774137),
    (0.9057660587451752,0.5254912075791537,0.43275873459164715),
    (0.908373881181583,0.5311929065572241,0.43135809840280354),
    (0.9109417598361584,0.5368971511480244,0.4300272629514147),
    (0.9134697945050229,0.5426039826373931,0.4287681995410676),
    (0.9159580766786966,0.5483133953613122,0.427582884408061),
    (0.918406714360436,0.5540254681019655,0.4264734659199734),
    (0.920815789044337,0.5597401318991866,0.42544197219331326),
    (0.923185402751968,0.5654574229117194,0.4244906346807608),
    (0.9255156452853701,0.57117730293536,0.4236216599374756),
    (0.9278066105957057,0.5768997483107496,0.42283734660270966),
    (0.9300583910203674,0.5826247165407025,0.4221400437118084),
    (0.9322710838845321,0.5883521843202228,0.421532205440667),
    (0.9344447826628309,0.5940820942482494,0.42101632047812315),
    (0.9365796074115389,0.5998145432024898,0.42059518470186885),
    (0.9386756106414039,0.6055491914200661,0.4202710532273208),
    (0.9407329079990889,0.6112860761093033,0.42004681014941947),
    (0.9427515974403947,0.6170251081457941,0.419925251874522),
    (0.9447317782783597,0.6227661886774984,0.41990925650123323),
    (0.9466735513738818,0.6285092089282214,0.42000178673868843),
    (0.948577019328259,0.6342540499722427,0.4202058929261213),
    (0.950442286678224,0.6400005824788457,0.42052471615622633),
    (0.952269460094059,0.6457486664253693,0.4209614915047042),
    (0.9540586485814028,0.6514981507772692,0.4215195513681973),
    (0.9558099636873687,0.6572488731335369,0.4222023289126453),
    (0.957523519711625,0.6630006593356775,0.4230133616338295),
    (0.9591994339231094,0.6687533230382895,0.4239562950315889),
    (0.9608378268202576,0.6745066655481706,0.42503488694474634),
    (0.9624388177292595,0.6802604359203214,0.4262529408144386),
    (0.9640025572336404,0.686014606369886,0.4276148072119741),
    (0.9655291501131507,0.6917687102359084,0.4291241972187295),
    (0.9670187052070511,0.6975222415498765,0.4307848779003112),
    (0.9684714420635883,0.7032756526710238,0.432602580636955),
    (0.969887449694959,0.7090281502755876,0.43458087361113173),
    (0.9712668759271996,0.7147794023366031,0.4367243491950651),
    (0.9726098975485952,0.7205292971234587,0.43903822072326804),
    (0.9739166462944493,0.7262771962206189,0.4415268443805185),
    (0.9751873647319815,0.7320235391053993,0.44419696999638364),
    (0.976422118501977,0.7377668019789888,0.44705152310836593),
    (0.9776211550505856,0.743507305958375,0.4500974402900779),
    (0.9787846444758076,0.7492444424019482,0.4533399563289745),
    (0.979912781124649,0.7549777591488878,0.45678485908186217),
    (0.9810057670051382,0.7607067748911029,0.4604381122172261),
    (0.9820638124589427,0.7664309800209004,0.46430586544042685),
    (0.9830871366480647,0.772149835034862,0.4683944597947778),
    (0.9840759680644438,0.777862768783022,0.4727104328428341),
    (0.9850305450645932,0.7835691765512458,0.47726052367398797),
    (0.9859511164349108,0.7892684180148672,0.482051677801156),
    (0.986837941989597,0.7949598150566919,0.4870910519071109),
    (0.9876912932031847,0.8006426494423506,0.4923860183959546),
    (0.9885114538797523,0.806316160345891,0.4979441696996811),
    (0.9892987208609487,0.8119795417184599,0.5037733222837119),
    (0.9900534047750122,0.817631939492967,0.5098815202887269),
    (0.9907758308290036,0.8232724486177281,0.5162770387389372),
    (0.9914663396464969,0.8289001099122617,0.5229683862391737),
    (0.9921252881529734,0.8345139067386849,0.5299643070746723),
    (0.9927530505111533,0.8401127614824955,0.5372737826181997),
    (0.9933500191084395,0.8456955318369103,0.5449060319388924),
    (0.9939166055985811,0.8512610068853106,0.5528705114957192),
    (0.9944532419995289,0.8568079029766595,0.5611769137853169),
    (0.9949603818492916,0.8623348593887721,0.5698351647982778),
    (0.9954385014213751,0.8678404337738685,0.5788554201186714),
    (0.995888101001087,0.8733230973793475,0.5882480594763102),
    (0.9963097062236235,0.8787812300335812,0.598023679526849),
    (0.9967038643819328,0.8842129359915843,0.6081924792498784),
    (0.9970711660056093,0.8896167313554539,0.6187665791074627),
    (0.9974122166294115,0.8949905310846435,0.629756636914948),
    (0.9977276580696293,0.900332300474433,0.6411740220319064),
    (0.9980181649921922,0.9056398806907502,0.653030236008046),
    (0.9982844468109042,0.9109109902345105,0.6653369171640384),
    (0.998527249400541,0.9161432172563653,0.6781058106449336),
    (0.9987473538110584,0.9213338193344665,0.6913479790447856),
    (0.9989455920713816,0.926480583420885,0.7050771598282567),
    (0.9991228257140827,0.9315804056984524,0.719304228506471),
    (0.9992799634576391,0.9366301716917528,0.7340405431868665),
    (0.9994179628202164,0.9416268368781807,0.7492983334302231),
    (0.9995378273305193,0.9465670622496658,0.7650891864197116),
    (0.9996406103616161,0.9514473509030297,0.7814245682270726),
    (0.9997274170282078,0.9562640621759412,0.7983158591709497),
    (0.9997994055779268,0.9610133596566172,0.8157740827679709),
    (0.9998577892638064,0.9656912154847488,0.8338098672328813),
    (0.9999038382247641,0.9702934688959152,0.8524336721964356),
    (0.999938880482452,0.9748157027943829,0.8716551251011398),
    (0.9999643011398209,0.9792518224639059,0.8914754650555298),
    (0.9999815565043686,0.9836016574903991,0.9119272363986172),
    (0.9999921487440342,0.9878556772720557,0.9329942410852291),
    (0.9999976528793963,0.9920102841092486,0.954691418579787),
    (0.9999997040126264,0.9960601712666104,0.9770247496863707),
    (1,1,1)]

_laguna_data = [(0,0,0),
    (0.01205234584720917,0.003029763753462933,0.012181626096951531),
    (0.024009539946322607,0.006071259935558802,0.024527387123832605),
    (0.035866440730114246,0.009126443061956018,0.03703306618444314),
    (0.04729762607741046,0.012115213030731464,0.049359976075078256),
    (0.057586222925058786,0.014854172715919293,0.0607419525372503),
    (0.06694864476127263,0.017396783846062337,0.07137513429213417),
    (0.07554539924055882,0.01978294402584963,0.08140455135188464),
    (0.08349921260398982,0.022043399849453856,0.09094088452074493),
    (0.09090230076455606,0.024201426447644277,0.10006644961635039),
    (0.09782726402759563,0.026275523336831332,0.10884566163480054),
    (0.10433072085315791,0.028280254420170754,0.11732805901239682),
    (0.11045872785701966,0.030227601536348247,0.1255535859071053),
    (0.11624909005293546,0.0321275203643479,0.13355466935505952),
    (0.12173326235826498,0.033988404056048256,0.14135797341541945),
    (0.12693772918185992,0.03581741956890588,0.1489856677551756),
    (0.13188503001178245,0.03762075784759309,0.1564563688045157),
    (0.13659452516120513,0.039403820364125944,0.16378583844680794),
    (0.141072454305137,0.04116828962921632,0.17097475770089335),
    (0.1453100556434715,0.042911366644519444,0.17800559072173824),
    (0.14932952119059353,0.04463924100511336,0.18489850239685307),
    (0.15317167856254224,0.046363927985756184,0.1916979886219688),
    (0.15695378782063363,0.048121379372063795,0.19854727460034177),
    (0.16068697884469937,0.049916373174243064,0.20546015073060347),
    (0.1643699913891173,0.051749969761059375,0.21243498534143554),
    (0.1680015753000074,0.05362321703760206,0.21947007668473517),
    (0.171580477835964,0.05553714464460113,0.22656363428986395),
    (0.1751054385384822,0.05749276021609239,0.23371376925238496),
    (0.17855634557918307,0.05948476947011581,0.24089306865268487),
    (0.18198846855459266,0.06153296686494651,0.2481757232289217),
    (0.1853440004947694,0.06361944980410128,0.2554832727539676),
    (0.18864053586587795,0.06575140656831951,0.26283888225744273),
    (0.1918768377203918,0.06792972119107672,0.270240209055012),
    (0.1950516005569509,0.07015521974800212,0.2776847077048969),
    (0.19816361084414752,0.07242872430746557,0.2851698524400147),
    (0.2012116551580298,0.07475101859134323,0.29269300720401253),
    (0.2041946477103067,0.07712289320546092,0.3002516097347243),
    (0.20711125160097407,0.07954500116988869,0.30784261523854095),
    (0.20996036856663,0.08201803801725344,0.3154632085687104),
    (0.21274086766326716,0.0845426384448496,0.32311040763419224),
    (0.21545164974974845,0.0871193979695036,0.330781156061913),
    (0.21809164513077897,0.08974886959926942,0.33847231838429787),
    (0.22065981898828652,0.09243156360429934,0.3461806871923468),
    (0.22315517358042655,0.09516794608789492,0.3539029856981725),
    (0.22557673812765736,0.09795843226046413,0.36163585078215427),
    (0.2279236305196177,0.10080341094442508,0.3693759313794449),
    (0.23019495734542628,0.10370319921015424,0.37711972850908315),
    (0.23238989671747737,0.10665807595857218,0.38486372748633263),
    (0.2345268980942713,0.10967725973537616,0.3926365439680771),
    (0.2365504868604819,0.11273534964820332,0.4003429532079294),
    (0.238510141631149,0.11585586811102358,0.40806313970208963),
    (0.24040294450058408,0.11903814931338677,0.4157902324987218),
    (0.24219367456990668,0.12226507073598716,0.4234605915637098),
    (0.24391601813606503,0.1255535388225773,0.4311296074228516),
    (0.24555776544271218,0.12889763921303682,0.43877314062710976),
    (0.24711856344548286,0.13229724398233222,0.44638743338344755),
    (0.24859812728348346,0.13575217363600767,0.45396872358841417),
    (0.24999624819266075,0.13926220082881066,0.4615132625375253),
    (0.25131277185780004,0.14282703792092935,0.4690172785834771),
    (0.25254763210456044,0.1464463552686267,0.47647704274551644),
    (0.25370083242604236,0.1501197711012369,0.4838888391225859),
    (0.2547724418803778,0.15384684894590167,0.49124896095330023),
    (0.25576263481775763,0.15762712190263156,0.4985537917876253),
    (0.256671633699501,0.16146005913367292,0.5057997009630258),
    (0.2574997476378383,0.16534508966646003,0.5129831227109632),
    (0.2582473663518394,0.16928160014262467,0.5201005506572569),
    (0.25891494774050716,0.17326892806967245,0.5271485188161344),
    (0.2595030362359562,0.17730637531328325,0.5341236445532047),
    (0.2600122519100311,0.18139320297889142,0.5410226134117421),
    (0.26044329189103516,0.1855286344171631,0.5478421886614692),
    (0.26079692943075405,0.18971185692596818,0.5545792163305715),
    (0.26107401286104104,0.19394202358522986,0.5612306301685113),
    (0.2612754647796992,0.19821825548017452,0.5677934572635889),
    (0.2614022807360477,0.20253964378308104,0.574264822753427),
    (0.26145547670184754,0.20690521151393437,0.5806418409217398),
    (0.26143629730006734,0.21131408108283156,0.586922084387382),
    (0.2613458899550244,0.2157652225908875,0.5931028718967769),
    (0.26118552536283374,0.22025762952898362,0.5991817620874171),
    (0.2609565379463418,0.2247902766186096,0.6051564305678001),
    (0.26066032352092167,0.22936212210629875,0.6110246726469832),
    (0.2602983368208157,0.23397211005738275,0.6167844056925289),
    (0.25987208889752456,0.2386191726395294,0.6224336711123918),
    (0.2593831444023063,0.24330223238679033,0.6279706359585527),
    (0.2588331187653245,0.24802020443520909,0.6333935941524168),
    (0.2582236752843457,0.25277199872142564,0.6387009673341687),
    (0.25755652213615376,0.25755652213615376,0.6438913053403845),
    (0.25683340932400517,0.26237268062489655,0.6489632863162156),
    (0.25605612557450874,0.26721938122879435,0.6539157164703832),
    (0.2552264951972686,0.27209553405906994,0.6587475294830181),
    (0.2543463749204884,0.27700005419912616,0.6634577855780492),
    (0.2534176507155041,0.281931863528974,0.6680456702733704),
    (0.25244223462289317,0.28688989246729985,0.6725104928233931),
    (0.25142206159240726,0.2918730816271209,0.6768516843697983),
    (0.2503590863485036,0.2968803833816268,0.6810687958173652),
    (0.2492552802927113,0.3019107633374408,0.685161495452635),
    (0.2481126284534672,0.30696320171316727,0.6891295663238806),
    (0.2469331264934148,0.3120366946217077,0.6929729034014257),
    (0.2457187777834614,0.3171302552554228,0.6966915105377286),
    (0.2444715905521714,0.3222429149737902,0.7002854972468944),
    (0.2431935751183215,0.3273737242937511,0.7037550753233622),
    (0.24188674121367712,0.33252175378345283,0.7071005553194535),
    (0.24055309540227218,0.33768609486056916,0.7103223429012672),
    (0.23919463860169712,0.3428658604968276,0.7134209351021088),
    (0.23781336371112405,0.3480601858307747,0.7163969164921863),
    (0.23641125335003424,0.35326822869117563,0.719250955282787),
    (0.23499027771086686,0.358489170033774,0.7219837993825133),
    (0.23355239252808202,0.36372221429442114,0.7245962724224467),
    (0.23209953716543294,0.36896658966183626,0.7270892697663422),
    (0.23063363282257518,0.3742215482734656,0.7294637545211065),
    (0.22915658086291754,0.3794863663404203,0.7317207535664513),
    (0.22767028692349917,0.3847603875722385,0.7338614363315556),
    (0.22617654503271886,0.39004283022836383,0.7358867424041327),
    (0.22467721703021667,0.3953330896382484,0.7377979577617484),
    (0.2231741475922071,0.40063060370725145,0.7395964472507636),
    (0.22166909046890945,0.4059347212734957,0.7412834090524179),
    (0.22016378045576354,0.41124482650765387,0.7428601074620256),
    (0.21865996757250636,0.4165604068212441,0.7443279899226184),
    (0.2171593456328344,0.4218809233457426,0.7456884474056067),
    (0.21566357540071182,0.42720585268355465,0.7469428894793073),
    (0.21417429698711327,0.4325347120148344,0.7480927858268339),
    (0.2126931163898208,0.4378670337655496,0.749139618753537),
    (0.21122160740748946,0.4432023692977609,0.7500848877900105),
    (0.2097613121845614,0.448540289988314,0.7509301096058482),
    (0.20831376369102125,0.45388043609364087,0.7516768970403499),
    (0.20688039586739843,0.4592223216353545,0.7523266332918073),
    (0.205462684423428,0.46456563851705784,0.7528809760660379),
    (0.20406204575599027,0.46991003832011463,0.7533414921657381),
    (0.2026798646394245,0.47525519078761685,0.7537097540231301),
    (0.20131749436953525,0.48060078326632105,0.7539873375186035),
    (0.1999762535878525,0.4859465119371221,0.7541758071818399),
    (0.1986574414967945,0.4912921175204994,0.7542767706178855),
    (0.19736231308856533,0.4966373241104904,0.7542917823090287),
    (0.19609209836247424,0.5019818839915194,0.7542224127744235),
    (0.1948479973327985,0.5073255642218205,0.7540702267992044),
    (0.19363118045081107,0.5126681460529614,0.7538367819047828),
    (0.19244278890196306,0.51800942392343,0.7535236262983259),
    (0.19128393599719734,0.5233492073224094,0.7531323010868413),
    (0.190155705413663,0.5286873140615781,0.7526643301222817),
    (0.18905915693391787,0.5340235840586475,0.7521212393890655),
    (0.18799531501510075,0.5393578451873037,0.7515045083767523),
    (0.1869651887660614,0.5446899673899351,0.7508156462229795),
    (0.18596931327646676,0.5500185062686053,0.750054339522918),
    (0.18500996460310068,0.5553472505573006,0.7492273820940937),
    (0.1840867479148016,0.5606721716193024,0.7483308778857248),
    (0.18320093015602273,0.5659942248978976,0.7473677087118122),
    (0.18235835405254308,0.5713140096820494,0.7463380702166279),
    (0.18361340438530863,0.5766040785520643,0.7443282017059937),
    (0.18496234908444778,0.5818782636746328,0.7423105765669775),
    (0.1864091805783031,0.5871375874950391,0.7402876641399138),
    (0.18795530551998116,0.5923817087895367,0.73826116907627),
    (0.1896027809926289,0.597610601944114,0.736233046068999),
    (0.1913536895217754,0.6028242331246114,0.7342053057101958),
    (0.19321010662508675,0.608022544835275,0.73218000533686),
    (0.19517408236313838,0.6132054482516462,0.7301592439547975),
    (0.19724772405803137,0.6183728642181306,0.7281451910546188),
    (0.19943308083787198,0.6235246684815001,0.7261400493284651),
    (0.20173220735473163,0.62866072384351,0.7241460769486983),
    (0.20414715284693713,0.6337808759926725,0.7221655851022319),
    (0.20667998070278082,0.6388849635546984,0.7202009460651979),
    (0.20933264539496724,0.6439727633429188,0.7182545508914389),
    (0.21210725735713631,0.6490441120116529,0.7163289040704768),
    (0.21500571461540996,0.6540987409699321,0.7144264937094108),
    (0.2180299710090632,0.6591363993982999,0.7125498874528056),
    (0.2211819935822154,0.6641568355237254,0.7107017190019045),
    (0.22446362929895186,0.6691597404513175,0.7088846396594229),
    (0.22787679758453255,0.6741448331790358,0.7071013903301108),
    (0.23142313494233047,0.679111711543667,0.7053546680368634),
    (0.23510455806085756,0.6840600921310255,0.7036473396845948),
    (0.23892295473914532,0.6889896786702238,0.7019823280512698),
    (0.24287963648170646,0.6938999423841101,0.7003623959456414),
    (0.2469763340592115,0.6987905336236846,0.6987905336236846),
    (0.25121457335037406,0.7036610266965915,0.6972697165688488),
    (0.2555958082852326,0.7085109771932815,0.6958029567360148),
    (0.26012141550942874,0.7133399222927745,0.694393300049529),
    (0.26479268896966107,0.7181473811288805,0.6930438236917185),
    (0.26961083444030637,0.7229328552216302,0.6917576331819463),
    (0.27457696401290715,0.7276958289785436,0.69053785924751),
    (0.27969209057191713,0.7324357702701958,0.6893876544890154),
    (0.2849571222816758,0.7371521310843175,0.688310189844253),
    (0.29037285711108685,0.7418443482623878,0.6873086508560671),
    (0.2959399774238261,0.7465118443223459,0.6863862337512103),
    (0.30165904466311205,0.7511540283706551,0.6855461413387209),
    (0.3075304941611031,0.7557702971065028,0.6847915787379276),
    (0.31355463010377427,0.7603600359204093,0.684125748947741),
    (0.31973162198411176,0.7649226205386718,0.6835518488758275),
    (0.32606083947154074,0.7694571923467624,0.6830727540568431),
    (0.3325440772761694,0.773963764676181,0.6826925320755441),
    (0.3391798838892037,0.7784412804885935,0.6824137804261192),
    (0.345966966344853,0.7828887979120471,0.6822391973040287),
    (0.3529052396122916,0.7873058322468949,0.6821721012415911),
    (0.35999457805782936,0.791691929975051,0.6822158437275301),
    (0.36723392144548617,0.7960463817141203,0.6823733601984845),
    (0.3746220837597788,0.8003684953850527,0.6826475556720404),
    (0.3821578037435943,0.8046576141027849,0.6830413274974299),
    (0.389839708220023,0.808913105770039,0.6835575444809818),
    (0.3976662334627543,0.8131343402689846,0.6841990027174403),
    (0.4056356825314762,0.8173207097377844,0.6849684506955578),
    (0.4137460984397827,0.8214715916600694,0.6858685175554246),
    (0.4219954346920726,0.8255864037117739,0.6869017978579488),
    (0.43038145635122593,0.8296645750560432,0.6880707946184061),
    (0.4389017633550123,0.833705555398749,0.6893779263889006),
    (0.44755379294713404,0.837708817409524,0.6908255233278013),
    (0.456334822427251,0.8416738590817423,0.6924158233866801),
    (0.46524197240144843,0.8456002060793015,0.6941509687322034),
    (0.47427221051759194,0.8494874140584916,0.6960330024160858),
    (0.48342235566606867,0.8533350709531172,0.6980638653039792),
    (0.49268908262259636,0.857142799210985,0.7002453932717663),
    (0.5020689271061349,0.8609102579699381,0.7025793146751893),
    (0.5115582912215026,0.8646371451617719,0.7050672480960831),
    (0.5211534492531372,0.8683231995326357,0.7077107003657496),
    (0.5308505537736568,0.8719682025688823,0.710511064863262),
    (0.5406454083384814,0.8755719170168387,0.713469474315513),
    (0.5505343810060228,0.8791343347601432,0.7165873635477702),
    (0.5605130941309429,0.8826553201954862,0.7198656520000917),
    (0.570577282062496,0.8861348434663459,0.7233052692209012),
    (0.5807225924581665,0.889572925610001,0.7269070274947051),
    (0.5909445937591988,0.8929696397991622,0.7306716218669728),
    (0.6012387827511126,0.8963251124449207,0.7345996304180153),
    (0.6116005921727565,0.8996395241572968,0.738691514773402),
    (0.6220253983383617,0.9029131105605662,0.7429476208372988),
    (0.6325085014502625,0.9061461559923614,0.7473681609750337),
    (0.6430452680965284,0.9093390284910283,0.7519533079087464),
    (0.6536308732776013,0.9124921123673928,0.7567030136117006),
    (0.6642605657417997,0.9156058743376463,0.7616171880240703),
    (0.6749295536414172,0.9186808325378082,0.7666956172215772),
    (0.6856330314128164,0.9217175615353894,0.7719379787440224),
    (0.6963661881136224,0.9247166924999836,0.7773438444838365),
    (0.7071242140604639,0.9276789128577605,0.7829126826335034),
    (0.7179023072382771,0.9306049658120554,0.7886438597103262),
    (0.7286955354794104,0.9334956144394788,0.7945365335995773),
    (0.7394993796029805,0.9363517727929471,0.8005900610487531),
    (0.7503089843437735,0.9391743196674979,0.8068034319893697),
    (0.761119632171154,0.9419642128065029,0.8131756232279921),
    (0.7719266566286959,0.9447224652007054,0.8197055325231819),
    (0.7827254107184195,0.9474501350640071,0.8263919523178938),
    (0.7935113056455582,0.9501483328819217,0.833233598652747),
    (0.8042799109687165,0.9528182431458107,0.8402291921710532),
    (0.8150264828784609,0.9554610082272131,0.8473770725416712),
    (0.8257467342462519,0.9580779117002054,0.8546758235074603),
    (0.8364361637268739,0.9606702141685073,0.8621237242014983),
    (0.8470907954589366,0.9632393288729301,0.8697193663799728),
    (0.8577061639655432,0.9657865751964958,0.8774608007215744),
    (0.8682780603115953,0.968313355720121,0.8853461604694947),
    (0.87880243703018,0.9708211309604589,0.893373586040606),
    (0.8892753265292789,0.9733113974380888,0.9015411565087744),
    (0.8996926734075714,0.9757856449108868,0.909846739180256),
    (0.910045030016059,0.9782440708347998,0.9182831631571076),
    (0.9203440545462892,0.9806919861701819,0.9268622824633515),
    (0.9305733176182466,0.9831279191562442,0.9355703538515282),
    (0.9407306681118847,0.9855538519712221,0.9444063890713731),
    (0.9508139224312147,0.9879717648032916,0.9533692891095606),
    (0.9608196050938197,0.9903833253445148,0.9624566335887379),
    (0.9707443234925962,0.9927902198388319,0.9716659435584898),
    (0.9805847683576848,0.9951941510355562,0.980994682502062),
    (0.9903377140895073,0.9975968361371285,0.9904402572742718),
    (1,1,1)]

if HAS_MPL:
    hesperia = ListedColormap(_hesperia_data, name="hesperia")
    hesperia_r = ListedColormap(list(reversed(_hesperia_data)),
                                name="hesperia_r")
    laguna = ListedColormap(_laguna_data, name="laguna")
    laguna_r = ListedColormap(list(reversed(_laguna_data)),
                              name="laguna_r")
    plt.register_cmap(cmap=hesperia)
    plt.register_cmap(cmap=hesperia_r)
    plt.register_cmap(cmap=laguna)
    plt.register_cmap(cmap=laguna_r)

    # Concatenate maps back to back so that the central value
    # is de-emphasized, and make the inverse scale "_r" as well:
    center_emph = ListedColormap((_hesperia_data[::-1][:192] + _laguna_data[1:][64:])[10:-10],
                                 name="center_emph")
    center_emph_r = ListedColormap(center_emph.colors[::-1],
                                   name="center_emph_r")
    plt.register_cmap(cmap=center_emph)
    plt.register_cmap(cmap=center_emph_r)

    # Now do the same thing, but to emphasize the central value instead:
    center_deemph = ListedColormap((_hesperia_data[:-1][64:] + _laguna_data[::-1][:192])[20:-20],
                                   name="center_deemph")
    center_deemph_r = ListedColormap(center_deemph.colors[::-1],
                                     name="center_deemph_r")
    plt.register_cmap(cmap=center_deemph)
    plt.register_cmap(cmap=center_deemph_r)

mpl_style = {

    # Lines
    'lines.linewidth': 1.7,
    'lines.antialiased': True,
    'lines.marker': '.',
    'lines.markersize': 5.,

    # Patches
    'patch.linewidth': 1.0,
    'patch.facecolor': '#348ABD',
    'patch.edgecolor': '#CCCCCC',
    'patch.antialiased': True,

    # images
    'image.origin': 'upper',

    # colormap
    'image.cmap': 'hesperia',

    # Font
    'font.size': 18.0,
    'text.latex.preamble': r'\usepackage{amsmath}',
    'axes.unicode_minus': False,

    # Axes
    'axes.facecolor': '#FFFFFF',
    'axes.edgecolor': '#AAAAAA',
    'axes.linewidth': 1.0,
    'axes.grid': False,
    'axes.titlesize': 'x-large',
    'axes.labelsize': 'large',
    'axes.labelcolor': 'k',
    'axes.axisbelow': True,

    # Ticks
    'xtick.major.size': 8,
    'xtick.minor.size': 4,
    'xtick.major.pad': 6,
    'xtick.minor.pad': 6,
    'xtick.color': '#565656',
    'xtick.direction': 'in',
    'ytick.major.size': 8,
    'ytick.minor.size': 4,
    'ytick.major.pad': 6,
    'ytick.minor.pad': 6,
    'ytick.color': '#565656',
    'ytick.direction': 'in',
    'xtick.labelsize': 'medium',
    'ytick.labelsize': 'medium',

    # Legend
    'legend.fancybox': True,
    'legend.loc': 'best',

    # Figure
    'figure.figsize': [8, 6],
    'figure.facecolor': '1.0',
    'figure.edgecolor': '0.50',
    'figure.subplot.hspace': 0.5,
    'figure.dpi': 300,

    # Other
    'savefig.dpi': 300,
}
