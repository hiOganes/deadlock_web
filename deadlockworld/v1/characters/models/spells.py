# Standart libraries
# Other libraries
from django.db import models

# Project libraries
from . import characters


class Spells(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_image = models.ImageField(
        upload_to="spells_description/%Y/%m/%d/", 
        blank=True, 
        null=True
        )
    cooldown = models.DecimalField(max_digits=5, decimal_places=2)
    activity = models.BooleanField(default=True, blank=True)
    characters = models.ForeignKey(
        'characters.Characters', 
        on_delete=models.CASCADE
        )
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="spells/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )
    slug = models.SlugField(max_length=255)
    spell_number = models.IntegerField()


    class Meta:
        ordering = ['characters_id']


    def __str__(self):
        return f'{self.title} #{self.spell_number}'




# Spells.objects.bulk_create([
#     Spells(title='siphon life', description="""Drain health from enemies in front of you while they are in the radius.""", description_image='spells_description/2024/11/10/abrams/siphon_life.jpg', cooldown=42, activity=True, characters_id=1, image='spells/2024/11/10/abrams/siphon_life.webp', slug='siphon_life', spell_number=1),
#     Spells(title='shoulder charge', description="""Charge forward, colliding with enemies and dragging them along. Hitting a wall will Stun enemies caught by Abrams. Speed increased after colliding with enemy Heroes.""", description_image='spells_description/2024/11/10/abrams/abrams/shoulder_charge.jpg', cooldown=37, activity=True, characters_id=1, image='spells/2024/11/10/shoulder_charge.webp', slug='shoulder_charge', spell_number=2),
#     Spells(title='infernal resilience', description="""Regenerate a portion of incoming damage over time.""", description_image='spells_description/2024/11/10/abrams/infernal_resilience.jpg', cooldown=0, activity=False, characters_id=1, image='spells/2024/11/10/abrams/infernal_resilience.webp', slug='infernal_resilience', spell_number=3),
#     Spells(title='seismic impact', description="""Leap high into the air and choose a ground location to crash into. When you hit the ground, all enemies in the radius are damaged and stunned. Press attack to crash down early.""", description_image='spells_description/2024/11/10/abrams/abrams/seismic_impact.jpg', cooldown=159, activity=True, characters_id=1, image='spells/2024/11/10/seismic_impact.webp', slug='seismic_impact', spell_number=4),
#     Spells(title='exploding uppercut', description="""Deal Light Melee damage to nearby units and send them flying back, causing area damage where they land. Does not damage allies.""", description_image='spells_description/2024/11/10/bebop/exploding_uppercut.jpg', cooldown=21, activity=True, characters_id=2, image='spells/2024/11/10/bebop/uppercut.webp', slug='uppercut', spell_number=1),
#     Spells(title='sticky bomb', description="""Attach a Sticky Bomb to a nearby target that deals explosive damage after a short fuse time. Gain +1% bomb damage for every attach and 5% for every dying hero hurt by Sticky Bomb in the last 12 seconds.""", description_image='spells_description/2024/11/10/bebop/stichy_bomb.jpg', cooldown=18, activity=True, characters_id=2, image='spells/2024/11/10/bebop/sticky_bomb.webp', slug='sticky_bomb', spell_number=2),
#     Spells(title='hook', description="""Launch out a hook that grabs and reels in the first enemy hero it hits, dealing damage. Target will be placed where you are facing. Cast using [M3] to target friendly heroes.""", description_image='spells_description/2024/11/10/bebop/hook.jpg', cooldown=23, activity=True, characters_id=2, image='spells/2024/11/10/bebop/hook.webp', slug='hook', spell_number=3),
#     Spells(title='hyper beam', description="""Charge up your laser to unleash a powerful torrent of energy that deals damage and slows enemies' movement and dashes. You have slow movement and turn rate for the duration. If activated in the air, you will hover while unleashing the beam.""", description_image='spells_description/2024/11/10/bebop/hyper_beam.jpg', cooldown=130, activity=True, characters_id=2, image='spells/2024/11/10/bebop/hyper_beam.webp', slug='hyper_beam', spell_number=4),
#     Spells(title='kinetic pulse', description="""Release an energy pulse that knocks enemies up into the air.""", description_image='spells_description/2024/11/10/dynamo/kinetic_pulse.jpg', cooldown=26, activity=True, characters_id=3, image='spells/2024/11/10/dynamo/kinetic_pulse.webp', slug='kinetic_pulse', spell_number=1),
#     Spells(title='quantum entanglement', description="""Dynamo briefly disappears into the void and then reappears a short distance away. On reappearing, your weapon is reloaded and has a fire rate bonus for the next clip (Max 8s). Can be cast with [M3] to also bring nearby allies and give them half fire rate bonus.""", description_image='spells_description/2024/11/10/dynamo/quantum_entanglement.jpg', cooldown=15, activity=True, characters_id=3, image='spells/2024/11/10/dynamo/quantum_entanglement.webp', slug='quantum_entanglement', spell_number=2),
#     Spells(title='rejuvenating aurora', description="""While channelling, restore health over time to you and any allies nearby.""", description_image='spells_description/2024/11/10/dynamo/rejuvenating_aurora.jpg', cooldown=48, activity=True, characters_id=3, image='spells/2024/11/10/dynamo/rej_aurora.webp', slug='rej_aurora', spell_number=3),
#     Spells(title='singularity', description="""Create a singularity in your hands that pulls in nearby enemies and damages them. Once it's finished, enemies get knocked into the air.""", description_image='spells_description/2024/11/10/dynamo/singularity.jpg', cooldown=191, activity=True, characters_id=3, image='spells/2024/11/10/dynamo/singularity.webp', slug='singularity', spell_number=4),
#     Spells(title='charged shot', description="""Charge up a powerful shot that pierces through enemies. Hold [1] or [LMB] to hold the shot.""", description_image='spells_description/2024/11/10/grey_talon/charged_shot.jpg', cooldown=17, activity=True, characters_id=4, image='spells/2024/11/10/grey_talon/charged_shot.webp', slug='charged_shot', spell_number=1),
#     Spells(title='rain of arrows', description="""Launches you high in the air, allowing you to glide slowly. While airborne, you gain Weapon Damage and multishot on your weapon. Press [SPACE] to cancel the glide. Can be alternate-casted to remain near the ground.""", description_image='spells_description/2024/11/10/grey_talon/rain_of_arrows.jpg', cooldown=35, activity=True, characters_id=4, image='spells/2024/11/10/grey_talon/rain_of_arrows.webp', slug='rain_of_arrows', spell_number=2),
#     Spells(title='immobilizing trap', description="""Throw out a trap that begins to arm itself. Once armed, the trap will trigger when an enemy enters its radius, immobilizing and then slowing them.""", description_image='spells_description/2024/11/10/grey_talon/immobilizing_trap.jpg', cooldown=37, activity=True, characters_id=4, image='spells/2024/11/10/grey_talon/immobilizing_trap.webp', slug='immobilizing_trap', spell_number=3),
#     Spells(title='guided owl', description="""After 1.5s cast time, launch a spirit owl that you control and which explodes on impact, damaging and stunning enemies. Hold [LMB] to accelerate the owl. Press [SPACE] to release control. Gain permanent Spirit Power for each enemy hero killed with Guided Owl (4s buffer window)""", description_image='spells_description/2024/11/10/grey_talon/guided_owl.jpg', cooldown=127, activity=True, characters_id=4, image='spells/2024/11/10/grey_talon/guided_owl.webp', slug='guided_owl', spell_number=4),
#     Spells(title='sleep dager', description="""Throw a dagger that damages and sleeps the target. Sleeping targets wake up shortly after being damaged. Throwing a Dagger does not break your invisibility. Sleep Dagger does not interrupt enemies' channeling abilities.""", description_image='spells_description/2024/11/10/haze/sleep_dager.jpg', cooldown=26, activity=True, characters_id=5, image='spells/2024/11/10/haze/sleep_dagger.webp', slug='sleep_dagger', spell_number=1),
#     Spells(title='smoke bomb', description="""Fade out of sight, becoming invisible and gaining sprint speed. Attacking removes invisibility. Close enemies can see through your invisibility.""", description_image='spells_description/2024/11/10/haze/smoke_bomb.jpg', cooldown=37, activity=True, characters_id=5, image='spells/2024/11/10/haze/smoke_bomb.webp', slug='smoke_bomb', spell_number=2),
#     Spells(title='fixation', description="""Shooting a target increases your bullet damage on that target. Gain one stack per bullet hit, two if the hit is a headshot.""", description_image='spells_description/2024/11/10/haze/fixation.jpg', cooldown=6, activity=True, characters_id=5, image='spells/2024/11/10/haze/fixation.webp', slug='fixation', spell_number=3),
#     Spells(title='bullet dance', description="""Enter a flurry, firing your weapon at nearby enemies with perfect accuracy. During the flurry, Haze gains a fire rate bonus and will evade some of the bullets shot at her.""", description_image='spells_description/2024/11/10/haze/bullet_dance.jpg', cooldown=138, activity=True, characters_id=5, image='spells/2024/11/10/haze/bullet_dance.webp', slug='bullet_dance', spell_number=4),
#     Spells(title='catalyst', description="""Spew napalm that slows enemy movement and amplifies the damage Infernus does to them""", description_image='spells_description/2024/11/10/infernus/catalyst.jpg', cooldown=25, activity=True, characters_id=6, image='spells/2024/11/10/infernus/catalyst.webp', slug='catalyst', spell_number=1),
#     Spells(title='flame dash', description="""Move forward at high speed and leave a flame trail that burns enemies. Infernus gains 50% slow resistance for the duration. Hold [LMB] to dash faster.""", description_image='spells_description/2024/11/10/infernus/flame_dash.jpg', cooldown=40, activity=True, characters_id=6, image='spells/2024/11/10/infernus/flame_dash.webp', slug='flame_dash', spell_number=2),
#     Spells(title='afterburn', description="""Your bullets build up to apply a burning effect on enemies. Infernus's bullets and abiliteis will refresh the duration.""", description_image='spells_description/2024/11/10/infernus/afterburn.jpg', cooldown=15, activity=True, characters_id=6, image='spells/2024/11/10/infernus/afterburn.webp', slug='afterburn', spell_number=3),
#     Spells(title='concussive combustion', description="""Turns you into a living bomb that explodes after a short delay, stunning all enemies in its radius.""", description_image='spells_description/2024/11/10/infernus/concussive_combustion.jpg', cooldown=127, activity=True, characters_id=6, image='spells/2024/11/10/infernus/concussive_combustion.webp', slug='concussive_combustion', spell_number=4),
#     Spells(title='kudzu bomb', description="""Summon a patch of choking vines that damages and slows enemies in its radius""", description_image='spells_description/2024/11/10/ivy/kudzu_bomb.jpg', cooldown=32, activity=True, characters_id=7, image='spells/2024/11/10/ivy/kudzu_bomb.webp', slug='kudzu_bomb', spell_number=1),
#     Spells(title="watcher's covenant", description="""Gain bonuses and automatically connect with a nearby ally to share them. Healing is replicated among all those connected. Connection requires line of sight. Press [2] to Lock on to a target.""", description_image='spells_description/2024/11/10/ivy/watchers_covenant.jpg', cooldown=37, activity=True, characters_id=7, image='spells/2024/11/10/ivy/watchers_covenant.webp', slug='watchers_covenant', spell_number=2),
#     Spells(title='stone form', description="""Turn yourself into impervious stone and smash into the ground, stunning and damaging enemies nearby. Heals you for a percentage of your max health. You have some air control before falling.""", description_image='spells_description/2024/11/10/ivy/stone_form.jpg', cooldown=42, activity=True, characters_id=7, image='spells/2024/11/10/ivy/stone_form.webp', slug='stone_form', spell_number=3),
#     Spells(title='air drop', description="""Take flight with an ally or a bomb. Drop your ally or bomb to cause a large explosion that causes movement slow. Ivy and ally gain a bullet shield when flying ends. While lifted, your ally gains bullet resist but cannot attack and deals -50% damage. Air Drop has faster cast time when targeting an ally. [LMB] to accellerate flying speed. [RMB] to drop ally/bomb.""", description_image='spells_description/2024/11/10/ivy/air_drop.jpg', cooldown=85, activity=True, characters_id=7, image='spells/2024/11/10/ivy/air_drop.webp', slug='air_drop', spell_number=4),
#     Spells(title='frost grenade', description="""Throw a grenade that explodes in a cloud of freezing ice, damaging and slowing enemies.""", description_image='spells_description/2024/11/10/kelvin/frost_grenade.jpg', cooldown=22, activity=True, characters_id=8, image='spells/2024/11/10/kelvin/frost_grenade.webp', slug='frost_grenade', spell_number=1),
#     Spells(title='ice path', description="""Kelvin creates a floating trail of ice and snow that gives movement bonuses to him and his allies. Kelvin gains 60% slow resistance for the duration. Enemies can also walk on the floating trail. Press [LEFT SHIFT]/[LEFT CTRL] to travel up or down while in Ice Path.""", description_image='spells_description/2024/11/10/kelvin/ice_path.jpg', cooldown=42, activity=True, characters_id=8, image='spells/2024/11/10/kelvin/ice_path.webp', slug='ice_path', spell_number=2),
#     Spells(title='arctic beam', description="""Shoot freezing cold energy out in front of you, damaging targets and building up movement and fire rate slow against them the longer you sustain the beam on them. You have reduced movement speed while using Arctic Beam. The beam may also claim Souls.""", description_image='spells_description/2024/11/10/kelvin/arctic_beam.jpg', cooldown=24, activity=True, characters_id=8, image='spells/2024/11/10/kelvin/arctic_beam.webp', slug='arctic_beam', spell_number=3),
#     Spells(title='frozen shelter', description="""Kelvin freezes the air around him, creating an impenetrable dome around himself. While in the dome, allies rapidly regenerate health and enemies are slowed. Objectives and Rejuvenator are frozen and invulnerable when under frozen shelter.""", description_image='spells_description/2024/11/10/kelvin/frozen_shelter.jpg', cooldown=127, activity=True, characters_id=8, image='spells/2024/11/10/kelvin/frozen_shelter.webp', slug='frozen_shelter', spell_number=4),
#     Spells(title='essence bomb', description="""Sacrifice some of your health to launch a bomb that deals damage after a brief arm time. Self damage type is Spirit and can be mitigated.""", description_image='spells_description/2024/11/10/lady_geist/essence_bomb.jpg', cooldown=10.5, activity=True, characters_id=9, image='spells/2024/11/10/lady_geist/essence_bomb.webp', slug='essence_bomb', spell_number=1),
#     Spells(title='life drain', description="""Create a tether that drains enemy health over time and heals you. Target must be in line of sight and within max range to drain. You can shoot and use other abilities during the drain, but your movement speed is reduced by half. Press [2] to cancel. Can be alt-casted on allied heroes.""", description_image='spells_description/2024/11/10/lady_geist/life_drain.jpg', cooldown=30, activity=True, characters_id=9, image='spells/2024/11/10/lady_geist/life_drain.webp', slug='life_drain', spell_number=2),
#     Spells(title='malice', description="""Sacrifice some of your health to launch blood shards that apply a stack of Malice. Each stack slows the victim and increases the damage they take from you. The slow effect decreases over time.""", description_image='spells_description/2024/11/10/lady_geist/malice.jpg', cooldown=6, activity=True, characters_id=9, image='spells/2024/11/10/lady_geist/malice.webp', slug='malice', spell_number=3),
#     Spells(title='soul exchange', description="""Swaps health levels with an enemy target. There is a minimum health percentage that enemies can be brought down to and a minimum amount of health received based on victims current health.""", description_image='spells_description/2024/11/10/lady_geist/soul_exchange.jpg', cooldown=170, activity=True, characters_id=9, image='spells/2024/11/10/lady_geist/soul_exchange.webp', slug='soul_exchange', spell_number=4),
#     Spells(title='ground strike', description="""Stomp the ground beneath you, damaging enemies in front of you. If you perform Ground Strike while airborne, you quickly dive towards the ground. Damage grows slower after 25m.""", description_image='spells_description/2024/11/10/lash/ground_strike.jpg', cooldown=19, activity=True, characters_id=10, image='spells/2024/11/10/lash/ground_strike.webp', slug='ground_strike', spell_number=1),
#     Spells(title='grapple', description="""Pull yourself through the air toward a target. Using Grapple also resets your limit of air jumps and dashes.""", description_image='spells_description/2024/11/10/lash/grapple.jpg', cooldown=42, activity=True, characters_id=10, image='spells/2024/11/10/lash/grapple.webp', slug='grapple.webp', spell_number=2),
#     Spells(title='flog', description="""Strike enemies with your whip, stealing life from them""", description_image='spells_description/2024/11/10/lash/flog.jpg', cooldown=26, activity=True, characters_id=10, image='spells/2024/11/10/lash/flog.webp', slug='flog', spell_number=3),
#     Spells(title='death slam', description="""Focus on enemies to connect whips to them. After channeling, connected enemies are lifted and stunned then slammed into the ground. Your victims and any enemies in the landing zone will be damaged and slowed. Press [LMB] to throw connected enemies early. Enemies that are not in line of sight or go out of range during the latch time will not be grabbed.""", description_image='spells_description/2024/11/10/lash/death_slam.jpg', cooldown=138, activity=True, characters_id=10, image='spells/2024/11/10/lash/death_slam.webp', slug='death_slam.webp', spell_number=4),
#     Spells(title='mini turret', description="""Deploy a Mini Turret that automatically shoots enemies. The turret expires after a limited lifetime. Turrets gain 30% of McGinnis's max health and have 60% Spirit Resist. They deal reduced damage to troopers and objectives.""", description_image='spells_description/2024/11/10/mcginnis/mini_turret.jpg', cooldown=18, activity=True, characters_id=11, image='spells/2024/11/10/mcginnis/tini_turret.webp', slug='tini_turret', spell_number=1),
#     Spells(title='medicinal specter', description="""Deploy a spirit that heals nearby units.""", description_image='spells_description/2024/11/10/mcginnis/medicinal_specter.jpg', cooldown=48, activity=True, characters_id=11, image='spells/2024/11/10/mcginnis/medicinal_specter.webp', slug='medicinal_specter', spell_number=2),
#     Spells(title='spectral wall', description="""Creates a wall that divides the terrain in half. On creation, the wall deals damage and applies slow to enemies nearby. After casting, press [LMB] or [3] to erupt the wall early.""", description_image='spells_description/2024/11/10/mcginnis/spectral_wall.jpg', cooldown=46, activity=True, characters_id=11, image='spells/2024/11/10/mcginnis/spectral_wall.webp', slug='spectral_wall', spell_number=3),
#     Spells(title='heavy barrage', description="""Unleashes a volley of rockets that home in on a targeted location.""", description_image='spells_description/2024/11/10/mcginnis/heavy_barrage.jpg', cooldown=140, activity=True, characters_id=11, image='spells/2024/11/10/mcginnis/heavy_barrage.webp', slug='heavy_barrage', spell_number=4),
#     Spells(title='tornado', description="""Transform yourself into a tornado that travels forward, damaging enemies and lifting them up in the air. After emerging from the tornado you gain bullet evasion.""", description_image='spells_description/2024/11/10/mirage/tornado.jpg', cooldown=32, activity=True, characters_id=12, image='spells/2024/11/10/mirage/tornado.webp', slug='tornado', spell_number=1),
#     Spells(title='fire scarabs', description="""Start launching fire scarabs. Each scarab can be launched separately, stealing max health from enemies and applying bullet resist reduction. Cannot apply multiple scarabs to the same enemy. The health gain from hitting heroes is 3x as effective as against non-heroes.""", description_image='spells_description/2024/11/10/mirage/fire_scarabs.jpg', cooldown=40, activity=True, characters_id=12, image='spells/2024/11/10/mirage/fire_scarabs.webp', slug='fire_scarabs', spell_number=2),
#     Spells(title="djinn's_mark", description="""Passive: Your shots apply an increasing multiplier on the target. When the multiplier on a target expires or you reach the max, it's consumed and the target suffers Spirit Damage and is briefly revealed on the map. The final damage is the base damage times the multiplier. Active: Consume multiplier or Djinn's Mark to deal its damage now.""", description_image='spells_description/2024/11/10/mirage/djinns_mark', cooldown=2.5, activity=False, characters_id=12, image='spells/2024/11/10/mirage/djinns_mark.webp', slug='djinns_mark', spell_number=3),
#     Spells(title='traveler', description="""Channeled. Target an ally or visible enemy hero on the minimap. then teleport to where they were when your channel started. After teleporting, you gain movement speed as well as fire rate until your next reload.""", description_image='spells_description/2024/11/10/mirage/traveler.jpg', cooldown=130, activity=True, characters_id=12, image='spells/2024/11/10/mirage/traveler.webp', slug='traveler', spell_number=4),
#     Spells(title='scorn', description="""Deal damage to nearby enemies and heal yourself based on the damage done. Heal is stronger against enemy heroes.""", description_image='spells_description/2024/11/10/mo_and_krill/scorn.jpg', cooldown=12.5, activity=True, characters_id=13, image='spells/2024/11/10/mo_and_krill/scorn.webp', slug='scorn', spell_number=1),
#     Spells(title='burrow', description="""Burrow underground, moving faster, and gaining spirit and bullet armor. Damage from enemy heroes will reduce the speed bonus. When you jump out, knock enemies into the air and perform a spin attack that damages and slows. Cooldown starts when Burrow ends.""", description_image='spells_description/2024/11/10/mo_and_krill/burrow.jpg', cooldown=37, activity=True, characters_id=13, image='spells/2024/11/10/mo_and_krill/burrow.webp', slug='burrow', spell_number=2),
#     Spells(title='sand blast', description="""Spray sand that disarms enemies in front of you and deals damage.""", description_image='spells_description/2024/11/10/mo_and_krill/sand_blast.jpg', cooldown=42, activity=True, characters_id=13, image='spells/2024/11/10/mo_and_krill/sand_blast.webp', slug='sand_blast', spell_number=3),
#     Spells(title='combo', description='Hold the target in place, stunning them and dealing damage during the channel. If they die during Combo, you permanently gain max health. 3s buffer window on kills to get this credit.', description_image='spells_description/2024/11/10/mo_and_krill/combo.jpg', cooldown=75, activity=True, characters_id=13, image='spells/2024/11/10/mo_and_krill/combo.webp', slug='combo', spell_number=4),
#     Spells(title='pulse grenade', description="""Throw a grenade that begins pulsing when it lands. Each pulse applies damage, movement slow, and stacking damage amplification for Paradox against the victim.""", description_image='spells_description/2024/11/10/paradox/pulse_grenade.jpg', cooldown=28, activity=True, characters_id=14, image='spells/2024/11/10/paradox/pulse_grenade.webp', slug='pulse_grenade', spell_number=1),
#     Spells(title='time wall', description="""Create a time warping wall that stops time for all enemy projectiles and bullets that touch it. Enemies that touch the wall will take damage as a percentage of their max health and be briefly slowed.""", description_image='spells_description/2024/11/10/paradox/time_wall.jpg', cooldown=37, activity=True, characters_id=14, image='spells/2024/11/10/paradox/time_wall.webp', slug='time_wall', spell_number=2),
#     Spells(title='kinetic carbine', description="""Start charging your weapon and gain increased movement speed once it's fully charged. Your next shot will release the energy, dealing spirit damage and applying a time stop to the enemy hit. The damage dealt is an amplification of your current weapon damage. You can slow time on yourself by pressing [RMB] while an empowered shot is available.""", description_image='spells_description/2024/11/10/paradox/kinetic_carbine.jpg', cooldown=30, activity=True, characters_id=14, image='spells/2024/11/10/paradox/kinetic_carbine.webp', slug='kinetic_carbine', spell_number=3),
#     Spells(title='paradoxical swap', description="""Fire a projectile that swaps your position with the target enemy hero. While the effect occurs, you gain spirit lifesteal and the enemy takes damage over time.""", description_image='spells_description/2024/11/10/paradox/paradoxical_swap.jpg', cooldown=65, activity=True, characters_id=14, image='spells/2024/11/10/paradox/paradoxical_swap.webp', slug='paradoxical_swap', spell_number=4),
#     Spells(title='barrage', description="""Channel to start launching projectiles that deal damage and apply 30% movement slow around their impact point. Each projectile landed on a hero grants you a stacking buff that amplifies all of your damage. If you cast it while in the air, you'll float and maintain any horizontal momentum you started with.""", description_image='spells_description/2024/11/10/pocket/barrage.jpg', cooldown=32, activity=True, characters_id=15, image='spells/2024/11/10/pocket/affliction.webp', slug='affliction', spell_number=1),
#     Spells(title='flying cloak', description="""Launch a sentient cloak that travels forward and damages enemies. You can press [2] to teleport to its location.""", description_image='spells_description/2024/11/10/pocket/flying_cloak.jpg', cooldown=32, activity=True, characters_id=15, image='spells/2024/11/10/pocket/flying_cloak.webp', slug='flying_cloak', spell_number=2),
#     Spells(title="enchanter's satchel", description="""Escape into your suitcase. When the duration ends, deal damage to nearby enemies. Duration can be ended early by performing any action.""", description_image='spells_description/2024/11/10/pocket/enchanters_satchel.jpg', cooldown=17, activity=True, characters_id=15, image='spells/2024/11/10/pocket/enchanters_satchel.webp', slug='enchanters_satchel', spell_number=3),
#     Spells(title='affliction', description="""Apply damage over time to all enemies nearby. Affliction's damage is non-lethal and does not apply item procs.""", description_image='spells_description/2024/11/10/pocket/affliction.jpg', cooldown=127, activity=True, characters_id=15, image='spells/2024/11/10/pocket/affliction.webp', slug='affliction', spell_number=4),
#     Spells(title='lightning ball', description="""Shoot a ball of lightning that travels in a straight line. Does damage to all targets in its radius. Slows down when damaging enemies and stops if it hits the world.""", description_image='spells_description/2024/11/10/seven/lightning_ball.jpg', cooldown=26, activity=True, characters_id=16, image='spells/2024/11/10/seven/lightning_ball.webp', slug='lightning_ball', spell_number=1),
#     Spells(title='static charge', description="""Apply a charge to a target enemy hero. After a short duration, the static charge stuns and damages enemies within the radius. Can be alt-casted on self.""", description_image='spells_description/2024/11/10/seven/static_charge.jpg', cooldown=42, activity=True, characters_id=16, image='spells/2024/11/10/seven/static_charge.webp', slug='static_charge', spell_number=2),
#     Spells(title='power_surge', description="""Power up your weapon with a shock effect, making your bullets proc shock damage on your target. This shock damage bounces to enemies near your target. Occurs once per burst shot.""", description_image='spells_description/2024/11/10/seven/power_surge.jpg', cooldown=48, activity=True, characters_id=16, image='spells/2024/11/10/seven/power_surge.webp', slug='power_surge.webp', spell_number=3),
#     Spells(title='storm_cloud', description="""Channel an expanding storm cloud around you that damages all enemies within its radius. Enemies do not take damage when they are out of line-of-sight. You have increased Bullet Resist during the channel.""", description_image='spells_description/2024/11/10/seven/storm_cloud.jpg', cooldown=148, activity=True, characters_id=16, image='spells/2024/11/10/seven/storm_cloud.webp', slug='storm_cloud', spell_number=4),
#     Spells(title='serrated knives', description="""Throw a knife that damages and bleeds an enemy. Each additional hit adds a stack and refreshes the bleed duration, causing the bleed to increase per stack.""", description_image='spells_description/2024/11/10/shiv/serrated_knives.jpg', cooldown=19, activity=True, characters_id=17, image='spells/2024/11/10/shiv/serrated_knives.webp', slug='serrated_knives', spell_number=1),
#     Spells(title='slice and dice', description="""Perform a dash forward, damaging enemies along the path.""", description_image='spells_description/2024/11/10/shiv/slice_and_dice.jpg', cooldown=16, activity=True, characters_id=17, image='spells/2024/11/10/shiv/slice_and_dice.webp', slug='slice_and_dice', spell_number=2),
#     Spells(title='bloodletting', description="""Take only a portion of incoming damage immediately and defer the rest to be taken over time. Activate to clear a portion of the deferred damage.""", description_image='spells_description/2024/11/10/shiv/bloodletting.jpg', cooldown=50, activity=True, characters_id=17, image='spells/2024/11/10/shiv/bloodletting.webp', slug='bloodletting', spell_number=3),
#     Spells(title='killing blow', description="""Activate to leap towards an enemy hero and instantly kill them if their health is below the kill threshold, otherwise deal 200 damage to them. Passive: Damaging enemies fills you with rage. While at full rage, Shiv gains increased damage and special properties on his other abilities.""", description_image='spells_description/2024/11/10/shiv/killing_blow.jpg', cooldown=95, activity=True, characters_id=17, image='spells/2024/11/10/shiv/killing_blow.webp', slug='killing_blow', spell_number=4),
#     Spells(title='stake', description="""Throw a stake that tethers enemies to the location where the stake lands. Enemy movement is restricted to the length of the tether.""", description_image='spells_description/2024/11/10/vindicta/stake.jpg', cooldown=42, activity=True, characters_id=18, image='spells/2024/11/10/vindicta/stake.webp', slug='stake', spell_number=1),
#     Spells(title='flight', description="""Leap into the air and fly. While in flight your weapon deals bonus spirit damage.""", description_image='spells_description/2024/11/10/vindicta/flight.jpg', cooldown=42, activity=True, characters_id=18, image='spells/2024/11/10/vindicta/flight.webp', slug='flight', spell_number=2),
#     Spells(title='crow familiar', description="""Your crow familiar deals impact damage and applies a bleed that deals damage based on the target's current health.""", description_image='spells_description/2024/11/10/vindicta/crow_familiar.jpg', cooldown=26, activity=True, characters_id=18, image='spells/2024/11/10/vindicta/crow_familiar.webp', slug='crow_familiar', spell_number=3),
#     Spells(title='assassinate', description="""Use your scoped rifle to fire a powerful shot over long distances. Deal only partial damage until fully charged after 1s of being scoped. Does bonus damage to enemies with less than 50% health remaining. Does 20% more damage on headshot. Landing a killing blow on a player with Assassinate grants you bonus unsecured souls.""", description_image='spells_description/2024/11/10/vindicta/assassinate.jpg', cooldown=53, activity=True, characters_id=18, image='spells/2024/11/10/vindicta/assassinate.webp', slug='assassinate', spell_number=4),
#     Spells(title='splatter', description="""Throw a ball of goo that deals damage and leaves puddles of goo behind that apply movement slow to enemies in the radius. Goo puddles linger on the ground and apply a movement slow to enemies walking on them.""", description_image='spells_description/2024/11/10/viscouse/splatter.jpg', cooldown=21, activity=True, characters_id=19, image='spells/2024/11/10/viscouse/splatter.webp', slug='splatter', spell_number=1),
#     Spells(title='the cube', description="""Encase the target in a cube of restorative goo that protects from damage, and increases health regen. Target is unable to take any new actions while cubed. Can be used on self. Press [SPACE] to escape early.""", description_image='spells_description/2024/11/10/viscouse/the_cube.jpg', cooldown=48, activity=True, characters_id=19, image='spells/2024/11/10/viscouse/the_cube.webp', slug='the_cube', spell_number=2),
#     Spells(title='puddle punch', description="""Materialize a fist in the world that punches units in the area and send them flying. Enemies will be dealt damage, have their dash distance reduced for a brief moment, and have their movement slowed. This is considered a Light Melee attack.""", description_image='spells_description/2024/11/10/viscouse/puddle_punch', cooldown=30, activity=True, characters_id=19, image='spells/2024/11/10/viscouse/puddle_punch.webp', slug='puddle_punch', spell_number=3),
#     Spells(title='goo ball', description="""Morph into a large goo ball that deals damage and stuns enemies on impact. The ball grants large amounts of Bullet and Spirit resist, bounces off walls and can double jump.""", description_image='spells_description/2024/11/10/viscouse/goo_ball.jpg', cooldown=95, activity=True, characters_id=19, image='spells/2024/11/10/viscouse/goo_ball.webp', slug='goo_ball.webp', spell_number=4),
#     Spells(title='alchemical flask', description="""Throw a flask that damages, slows, and reduces the weapon damage and stamina of enemies it hits.""", description_image='spells_description/2024/11/10/warden/alchemical_flask.jpg', cooldown=12, activity=True, characters_id=20, image='spells/2024/11/10/warden/alchemical_flask.webp', slug='alchemical_flask.webp', spell_number=1),
#     Spells(title='willpower', description="""Gain a spirit shield and bonus movement speed.""", description_image='spells_description/2024/11/10/warden/willpower.jpg', cooldown=42, activity=True, characters_id=20, image='spells/2024/11/10/warden/willpower.webp', slug='willpower.webp', spell_number=2),
#     Spells(title='binding word', description="""Curse an enemy hero. If they don't move away from their initial position within the escape time, they will be damaged and immobilized.""", description_image='spells_description/2024/11/10/warden/binding_word.jpg', cooldown=37, activity=True, characters_id=20, image='spells/2024/11/10/warden/binding_word.webp', slug='binding_word', spell_number=3),
#     Spells(title='last_stand', description="""After charging for 2s, release pulses that damage enemies and heal you based on the damage done.""", description_image='spells_description/2024/11/10/warden/last_stand.jpg', cooldown=138, activity=True, characters_id=20, image='spells/2024/11/10/warden/last_stand.webp', slug='last_stand', spell_number=4),
#     Spells(title='card trick', description="""Deal weapon damage to summon cards. Activate to throw a card that flies towards the enemy or point under your crosshair.""", description_image='spells_description/2024/11/10/wraith/card_trick.jpg', cooldown=0.65, activity=True, characters_id=21, image='spells/2024/11/10/wraith/card_trick.webp', slug='card_trick', spell_number=1),
#     Spells(title='project mind', description="""Teleport to the targeted location.""", description_image='spells_description/2024/11/10/wraith/project_mind.jpg', cooldown=48, activity=True, characters_id=21, image='spells/2024/11/10/wraith/project_mind.webp', slug='project_mind', spell_number=2),
#     Spells(title='full auto', description="""Temporarily boosts your fire rate. Nearby allies receive half the fire rate bonus.""", description_image='spells_description/2024/11/10/wraith/full_auto.jpg', cooldown=48, activity=True, characters_id=21, image='spells/2024/11/10/wraith/full_auto.webp', slug='full_auto', spell_number=3),
#     Spells(title='telekinesis', description="""Lift an enemy hero into the air, stunning them for a short time. When the lift ends, the target receives Telekinesis damage.""", description_image='spells_description/2024/11/10/wraith/telekinesis.jpg', cooldown=100, activity=True, characters_id=21, image='spells/2024/11/10/wraith/telekinesis.webp', slug='telekinesis', spell_number=4),
#     Spells(title='power slash', description="""Channel to increase damage over 1.4 seconds, then release a fully-charged sword strike. Press [1] or [-] to trigger the strike early, dealing partial damage.""", description_image='spells_description/2024/11/10/yamato/power_slash.jpg', cooldown=10.5, activity=True, characters_id=22, image='spells/2024/11/10/yamato/power_slash.webp', slug='power_slash', spell_number=1),
#     Spells(title='flying strike', description="""Throw a grappling hook to reel yourself towards an enemy, damaging and slowing the target when you arrive.""", description_image='spells_description/2024/11/10/yamato/flying_strike.jpg', cooldown=21, activity=True, characters_id=22, image='spells/2024/11/10/yamato/flying_strike.webp', slug='flying_strike', spell_number=2),
#     Spells(title='crimson slash', description="""Slash enemies in front of you, damaging them and slowing their fire rate. If any enemy heroes are hit, you heal.""", description_image='spells_description/2024/11/10/yamato/crimson_slash.jpg', cooldown=11.5, activity=True, characters_id=22, image='spells/2024/11/10/yamato/crimson_slash.webp', slug='crimson_slash', spell_number=3),
#     Spells(title='shadow transformation', description="""Become infused with Yamato's shadow soul. After an initial invincible transformation, your abilities are refreshed and are 60% faster, and you gain damage resists and immunity to negative status effects. You are unable to die in this mode.""", description_image='spells_description/2024/11/10/yamato/shadow_transformation.jpg', cooldown=85, activity=True, characters_id=22, image='spells/2024/11/10/yamato/shadow_transformation.webp', slug='shadow_transformation', spell_number=4)
# ])