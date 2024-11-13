# Standart libraries
# Other libraries
from django.db import models

# Project libraries


class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to="shop/%Y/%m/%d/", 
        default=None, blank=True, 
        null=True
        )
    category = models.CharField(max_length=255)
    activity = models.BooleanField(default=False, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)

    class Meta:
        ordering = ['price']
        indexes = [models.Index(fields=['price'])]



# Shop.objects.bulk_create([
#     Shop(title='ammo scavenger', description="""{'Ammo': +15%, 'Bonus Health': +40}""", price=500, image='shop/spirit/2024/11/12/500/ammo_scavenger.png', category='spirit', activity=False, slug='ammo_scavenger'),
#     Shop(title='extra charge', description="""{'Bonus Ability Charges': +1, 'Cooldown Reduction for Charged Abilities': +10%, 'Weapon Damage': +6%}""", price=500, image='shop/spirit/2024/11/12/500/extra_charge.png', category='spirit', activity=False, slug='extra_charge'),
#     Shop(title='extra spirit', price=500, image='shop/spirit/2024/11/12/500/extra_spirit.png', category='spirit', activity=False, slug='extra_spirit'),
#     Shop(title='infuser', price=500, image='shop/spirit/2024/11/12/500/infuser.png', category='spirit', activity=True, slug='infuser'),
#     Shop(title='mystic burst', price=500, image='shop/spirit/2024/11/12/500/mystic_burst.png', category='spirit', activity=False, slug='mystic_burst'),
#     Shop(title='mystic reach', price=500, image='shop/spirit/2024/11/12/500/mystic_reach.png', category='spirit', activity=False, slug='mystic_reach'),
#     Shop(title='spirit strike', price=500, image='shop/spirit/2024/11/12/500/spirit_strike.png', category='spirit', activity=False, slug='spirit_strike'),
#     Shop(title='bullet resist shredder', price=1250, image='shop/spirit/2024/11/12/500/bullet_resist_shredder.png', category='spirit', activity=False, slug='bullet_resist_shredder'),
#     Shop(title='cold front', price=1250, image='shop/spirit/2024/11/12/500/cold_front.png', category='spirit', activity=True, slug='cold_front'),
#     Shop(title='decay', price=1250, image='shop/spirit/2024/11/12/500/decay.png', category='spirit', activity=True, slug='decay'),
#     Shop(title='duration extender', price=1250, image='shop/spirit/2024/11/12/500/duration_extender.png', category='spirit', activity=False, slug='duration_extender'),
#     Shop(title='improved cooldown', price=1250, image='shop/spirit/2024/11/12/500/improved_cooldown.png', category='spirit', activity=False, slug='improved_cooldown'),
#     Shop(title='mystic vulnerability', price=1250, image='shop/spirit/2024/11/12/500/', category='spirit', activity=False, slug='mystic_vulnerability'),
#     Shop(title='quicksilver reload', price=1250, image='shop/spirit/2024/11/12/500/quicksilver_reload.png', category='spirit', activity=False, slug='quicksilver_reload'),
#     Shop(title='slowing hex', price=1750, image='shop/spirit/2024/11/12/500/slowing_hex.png', category='spirit', activity=False, slug='slowing_hex'),
#     Shop(title='suppressor', price=1250, image='shop/spirit/2024/11/12/500/suppressor.png', category='spirit', activity=False, slug='suppressor'),
#     Shop(title='withering_whip', price=1250, image='shop/spirit/2024/11/12/500/withering_whip.png', category='spirit', activity=True, slug='withering_whip'),
#     Shop(title='ethereal shift', price=3000, image='shop/spirit/2024/11/12/500/ethereal_shift.png', category='spirit', activity=True, slug='ethereal_shift'),
#     Shop(title='improved burst', price=3500, image='shop/spirit/2024/11/12/500/improved_burst.png', category='spirit', activity=False, slug='improved_burst'),
#     Shop(title='improved reach', price=3500, image='shop/spirit/2024/11/12/500/improved_reach.png', category='spirit', activity=False, slug='improved_reach'),
#     Shop(title='improved spirit', price=3500, image='shop/spirit/2024/11/12/500/improved_spirit.png', category='spirit', activity=False, slug='improved_spirit'),
#     Shop(title='knockdown', price=3000, image='shop/spirit/2024/11/12/500/knockdown.png', category='spirit', activity=True, slug='knockdown'),
#     Shop(title='mystic slow', price=4250, image='shop/spirit/2024/11/12/500/mystic_slow.png', category='spirit', activity=False, slug='mystic_slow'),
#     Shop(title='rapid recharge', price=3500, image='shop/spirit/2024/11/12/500/rapid_recharge.png', category='spirit', activity=False, slug='rapid_recharge'),
#     Shop(title='silence glyph', price=3000, image='shop/spirit/2024/11/12/500/silence_glyph.png', category='spirit', activity=True, slug='silence_glyph'),
#     Shop(title='superior cooldown', price=4250, image='shop/spirit/2024/11/12/500/superior_cooldown.png', category='spirit', activity=False, slug='superior_cooldown'),
#     Shop(title='superior duration', price=4250, image='shop/spirit/2024/11/12/500/superior_duration.png', category='spirit', activity=False, slug='superior_duration'),
#     Shop(title='surge of power', price=3000, image='shop/spirit/2024/11/12/500/surge_of_power.png', category='spirit', activity=False, slug='surge_of_power'),
#     Shop(title='torment pulse', price=3000, image='shop/spirit/2024/11/12/500/torment_pulse.png', category='spirit', activity=False, slug='torment_pulse'),
#     Shop(title='boundless spirit', price=9700, image='shop/spirit/2024/11/12/500/boundless_spirit.png', category='spirit', activity=False, slug='boundless_spirit'),
#     Shop(title='curse', price=6200, image='shop/spirit/2024/11/12/500/curse.png', category='spirit', activity=True, slug='curse'),
#     Shop(title="diviner's kevlar", price=6200, image='shop/spirit/2024/11/12/500/diviners_kevlar.png', category='spirit', activity=False, slug='diviners_kevlar'),
#     Shop(title='echo shard', price=6200, image='shop/spirit/2024/11/12/500/echo_shard.png', category='spirit', activity=True, slug='echo_shard'),
#     Shop(title='escalating exposure', price=7450, image='shop/spirit/2024/11/12/500/escalating_exposure.png', category='spirit', activity=False, slug='escalating_exposure'),
#     Shop(title='magic carpet', price=6200, image='shop/spirit/2024/11/12/500/magic_carpet.png', category='spirit', activity=True, slug='magic_carpet'),
#     Shop(title='mystic reverb', price=6200, image='shop/spirit/2024/11/12/500/mystic_reverb.png', category='spirit', activity=False, slug='mystic_reverb'),
#     Shop(title='refresher', price=6200, image='shop/spirit/2024/11/12/500/refresher.png', category='spirit', activity=True, slug='refresher'),
#     Shop(title='healing rite', price=500, image='shop/vitality/2024/11/12/500/healing_rite.png', category='vitality', activity=True, slug='healing_rite'),
#     Shop(title='enduring spirit', description="""{'Bonus Health': +75, 'Spirit Lifesteal': +10%, 'Spirit Power': +4, 'IS COMPONENT OF': 'Slowing Hex'}""", price=500, image='shop/vitality/2024/11/12/500/enduring_spirit.png', category='vitality', activity=False, slug='enduring_spirit'),
#     Shop(title='extra health', description="""{'Bonus Health': +160, 'Weapon Damage': +7%, 'IS COMPONENT OF': Fortitude}""", price=500, image='shop/vitality/2024/11/12/500/extra_health.png', category='vitality', activity=False, slug='extra_health'),
#     Shop(title='extra regen', price=500, image='shop/vitality/2024/11/12/500/extra_regen.png', category='vitality', activity=False, slug='extra_regen'),
#     Shop(title='extra stamina', price=500, image='shop/vitality/2024/11/12/500/extra_stamina.png', category='vitality', activity=False, slug='extra_stamina'),
#     Shop(title='melee lifesteal', price=500, image='shop/vitality/2024/11/12/500/melee_lifesteal.png', category='vitality', activity=False, slug='melee_lifesteal'),
#     Shop(title='sprint boots', price=500, image='shop/vitality/2024/11/12/500/sprint_boots.png', category='vitality', activity=False, slug='sprint_boots'),
#     Shop(title='bullet armor', price=1250, image='shop/vitality/2024/11/12/500/bullet_armor.png', category='vitality', activity=False, slug='bullet_armor'),
#     Shop(title='bullet lifesteal', price=1250, image='shop/vitality/2024/11/12/500/bullet_lifesteal.png', category='vitality', activity=False, slug='bullet_lifesteal'),
#     Shop(title='combat barrier', price=1250, image='shop/vitality/2024/11/12/500/combat_barrier.png', category='vitality', activity=False, slug='combat_barrier'),
#     Shop(title='debuff reducer', price=1250, image='shop/vitality/2024/11/12/500/debuff_reducer.png', category='vitality', activity=False, slug='debuff_reducer'),
#     Shop(title='divine barrier', price=1250, image='shop/vitality/2024/11/12/500/divine_barrier.png', category='vitality', activity=True, slug='divine_barrier'),
#     Shop(title="enchanter's barrier", price=1250, image='shop/vitality/2024/11/12/500/enchanters_barrier.png', category='vitality', activity=False, slug='enchanters_barrier'),
#     Shop(title='enduring speed', price=1750, image='shop/vitality/2024/11/12/500/enduring_speed', category='vitality', activity=False, slug='enduring_speed'),
#     Shop(title='healbane', price=1250, image='shop/vitality/2024/11/12/500/healbane.png', category='vitality', activity=False, slug='healbane'),
#     Shop(title='healing booster', price=1250, image='shop/vitality/2024/11/12/500/healing_booster.png', category='vitality', activity=False, slug='healing_booster'),
#     Shop(title='healing nova', price=1750, image='shop/vitality/2024/11/12/500/healing_nova.png', category='vitality', activity=True, slug='healing_nova'),
#     Shop(title='reactive barrier', price=1250, image='shop/vitality/2024/11/12/500/reactive_barrier.png', category='vitality', activity=False, slug='reactive_barrier'),
#     Shop(title='restorative locket', price=1250, image='shop/vitality/2024/11/12/500/restorative_locket.png', category='vitality', activity=True, slug='restorative_locket'),
#     Shop(title='return fire', price=1250, image='shop/vitality/2024/11/12/500/return_fire.png', category='vitality', activity=True, slug='return_fire'),
#     Shop(title='return fire', price=1250, image='shop/vitality/2024/11/12/500/return_fire.png', category='vitality', activity=True, slug='return_fire'),
#     Shop(title='spirit armor', price=1250, image='shop/vitality/2024/11/12/500/spirit_armor.png', category='vitality', activity=False, slug='spirit_armor'),
#     Shop(title='spirit lifesteal', price=1250, image='shop/vitality/2024/11/12/500/spirit_lifesteal.png', category='vitality', activity=False, slug='spirit_lifesteal'),
#     Shop(title='debuff remover', price=4250, image='shop/vitality/2024/11/12/500/debuff_remover.png', category='vitality', activity=True, slug='debuff_remover'),
#     Shop(title='fortitude', price=3500, image='shop/vitality/2024/11/12/500/fortitude.png', category='spirit', activity=False, slug='fortitude'),
#     Shop(title='improved bullet armor', price=4250, image='shop/vitality/2024/11/12/500/improved_bullet_armor.png', category='vitality', activity=False, slug='improved_bullet_armor'),
#     Shop(title='improved_spirit_armor', price=4250, image='shop/vitality/2024/11/12/500/improved_spirit_armor.png', category='vitality', activity=False, slug='improved_spirit_armor'),
#     Shop(title='lifestrike', price=3500, image='shop/vitality/2024/11/12/500/lifestrike.png', category='vitality', activity=False, slug='lifestrike'),
#     Shop(title='majestic leap', price=3000, image='shop/vitality/2024/11/12/500/majestic_leap.png', category='vitality', activity=True, slug='majestic_leap'),
#     Shop(title='metal skin', price=3000, image='shop/vitality/2024/11/12/500/metal_skin.png', category='vitality', activity=True, slug='metal_skin'),
#     Shop(title='rescue beam', price=3000, image='shop/vitality/2024/11/12/500/rescue_beam.png', category='vitality', activity=True, slug='rescue_beam'),
#     Shop(title='superior stamina', price=3500, image='shop/vitality/2024/11/12/500/superior_stamina.png', category='vitality', activity=False, slug='superior_stamina'),
#     Shop(title='veil walker', price=3000, image='shop/vitality/2024/11/12/500/veil_walker.png', category='vitality', activity=False, slug='veil_walker'),
#     Shop(title='colossus', price=6200, image='shop/vitality/2024/11/12/500/colossus.png', category='vitality', activity=True, slug='colossus'),
#     Shop(title='inhibitor', price=6200, image='shop/vitality/2024/11/12/500/inhibitor.png', category='vitality', activity=False, slug='inhibitor'),
#     Shop(title='leech', price=6200, image='shop/vitality/2024/11/12/500/leech.png', category='vitality', activity=False, slug='leech'),
#     Shop(title='phantom strike', price=6200, image='shop/vitality/2024/11/12/500/phantom_strike.png', category='vitality', activity=True, slug='phantom_strike'),
#     Shop(title='siphon bullets', price=6200, image='shop/vitality/2024/11/12/500/siphon_bullets.png', category='vitality', activity=False, slug='siphon_bullets'),
#     Shop(title='unstoppable', price=6200, image='shop/vitality/2024/11/12/500/unstoppable.png', category='vitality', activity=True, slug='unstoppable'),
#     Shop(title='basic magazine', price=500, description="""{'Ammo': '+26%', 'Weapon Damage': '+15%', 'IS COMPONENT OF': 'Titanic Magazine'}""", image='shop/weapon/2024/11/12/500/basic_magazine.png', category='weapon', activity=False, slug='basic_magazine'),
#     Shop(title='close quarters', price=500, description="""{'Bullet Resist': '+5%', 'IS COMPONENT OF': 'Point Blank'}""", image='shop/weapon/2024/11/12/500/close_quarters.png', category='weapon', activity=False, slug='close_quarters'),
#     Shop(title='headshot booster', price=500, image='shop/weapon/2024/11/12/500/headshot_booster.png', category='weapon', activity=False, slug='headshot_booster'),
#     Shop(title='high velocity mag', price=500, image='shop/weapon/2024/11/12/500/high-velocity_mag.png', category='weapon', activity=False, slug='high-velocity_mag'),
#     Shop(title='hollow point ward', price=500, image='shop/weapon/2024/11/12/500/hollow_point_ward.png', category='weapon', activity=False, slug='hollow_point_ward'),
#     Shop(title='monster rounds', price=500, image='shop/weapon/2024/11/12/500/monster_rounds.png', category='weapon', activity=False, slug='monster_rounds'),
#     Shop(title='rapid rounds', price=500, image='shop/weapon/2024/11/12/500/rapid_rounds.png', category='weapon', activity=False, slug='rapid_rounds'),
#     Shop(title='restorative shot', price=500, image='shop/weapon/2024/11/12/500/restorative_shot.png', category='weapon', activity=False, slug='restorative_shot'),
#     Shop(title='active reload', price=1250, image='shop/weapon/2024/11/12/500/active_reload.png', category='weapon', activity=False, slug='active_reload'),
#     Shop(title='berserker', price=1250, image='shop/weapon/2024/11/12/500/berserker.png', category='weapon', activity=False, slug='berserker'),
#     Shop(title='fleetfoot', price=1250, image='shop/weapon/2024/11/12/500/fleetfoot.png', category='weapon', activity=True, slug='fleetfoot'),
#     Shop(title='kinetic dash', price=1250, image='shop/weapon/2024/11/12/500/kinetic_dash.png', category='weapon', activity=False, slug='kinetic_dash'),
#     Shop(title='long range', price=1250, image='shop/weapon/2024/11/12/500/long_range.png', category='weapon', activity=False, slug='long_range'),
#     Shop(title='melee charge', price=1250, image='shop/weapon/2024/11/12/500/melee_charge.png', category='weapon', activity=False, slug='melee_charge'),
#     Shop(title='mystic shot', price=1250, image='shop/weapon/2024/11/12/500/mystic_shot.png', category='weapon', activity=False, slug='mystic_shot'),
#     Shop(title='slowing bullets', price=1250, image='shop/weapon/2024/11/12/500/slowing_bullets.png', category='weapon', activity=False, slug='slowing_bullets'),
#     Shop(title='soul shredder bullets', price=1250, image='shop/weapon/2024/11/12/500/soul_shredder_bullets.png', category='weapon', activity=False, slug='soul_shredder_bullets'),
#     Shop(title='swift striker', price=1250, image='shop/weapon/2024/11/12/500/swift_striker.png', category='weapon', activity=False, slug='swift_striker'),
#     Shop(title='alchemical fire', price=3000, image='shop/weapon/2024/11/12/500/alchemical_fire.png', category='weapon', activity=True, slug='alchemical_fire'),
#     Shop(title='burst fire', price=3000, image='shop/weapon/2024/11/12/500/burst_fire.png', category='weapon', activity=False, slug='burst_fire'),
#     Shop(title='escalating resilience', price=3000, image='shop/weapon/2024/11/12/500/escalating_resilience.png', category='weapon', activity=False, slug='escalating_resilience'),
#     Shop(title='headhunter', price=3500, image='shop/weapon/2024/11/12/500/headhunter.png', category='weapon', activity=False, slug='headhunter'),
#     Shop(title='heroic aura', price=3000, image='shop/weapon/2024/11/12/500/heroic_aura.png', category='weapon', activity=True, slug='heroic_aura'),
#     Shop(title="hunter's aura", price=3000, image='shop/weapon/2024/11/12/500/hunters_aura.png', category='weapon', activity=False, slug='hunters_aura'),
#     Shop(title='intensifying magazine', price=3000, image='shop/weapon/2024/11/12/500/intensifying_magazine.png', category='weapon', activity=False, slug='intensifying_magazine'),
#     Shop(title='point blank', price=3500, image='shop/weapon/2024/11/12/500/point_blank.png', category='weapon', activity=False, slug='point_blank'),
#     Shop(title='pristine emblem', price=3500, image='shop/weapon/2024/11/12/500/pristine_emblem.png', category='weapon', activity=False, slug='pristine_emblem'),
#     Shop(title='sharpshooter', price=4250, image='shop/weapon/2024/11/12/500/sharpshooter.png', category='weapon', activity=False, slug='sharpshooter'),
#     Shop(title='tesla bullets', price=3000, image='shop/weapon/2024/11/12/500/tesla_bullets.png', category='weapon', activity=False, slug='tesla_bullets'),
#     Shop(title='titanic magazine', price=3500, image='shop/weapon/2024/11/12/500/titanic_magazine.png', category='weapon', activity=False, slug='titanic_magazine'),
#     Shop(title='toxic bullets', price=3000, image='shop/weapon/2024/11/12/500/toxic_bullets.png', category='weapon', activity=False, slug='toxic_bullets'),
#     Shop(title='warp stone', price=3000, image='shop/weapon/2024/11/12/500/warp_stone.png', category='weapon', activity=True, slug='warp_stone'),
#     Shop(title='crippling headshot', price=6200, image='shop/weapon/2024/11/12/500/crippling_headshot.png', category='weapon', activity=False, slug='crippling_headshot'),
#     Shop(title='frenzy', price=6200, image='shop/weapon/2024/11/12/500/frenzy.png', category='weapon', activity=False, slug='frenzy'),
#     Shop(title='glass cannon', price=6200, image='shop/weapon/2024/11/12/500/glass_cannon.png', category='weapon', activity=False, slug='glass_cannon'),
#     Shop(title='lucky shot', price=6200, image='shop/weapon/2024/11/12/500/lucky_shot.png', category='weapon', activity=False, slug='lucky_shot'),
#     Shop(title='ricochet', price=6200, image='shop/weapon/2024/11/12/500/ricochet.png', category='weapon', activity=False, slug='ricochet'),
#     Shop(title='shadow weave', price=6200, image='shop/weapon/2024/11/12/500/shadow_weave.png', category='weapon', activity=True, slug='shadow_weave'),
#     Shop(title='silencer', price=6200, image='shop/weapon/2024/11/12/500/silencer.png', category='weapon', activity=True, slug='silencer'),
#     Shop(title='spiritual overflow', price=6200, image='shop/weapon/2024/11/12/500/spiritual_overflow.png', category='weapon', activity=False, slug='spiritual_overflow'),
#     Shop(title='vampiric burst', price=6200, image='shop/weapon/2024/11/12/500/vampiric_burst.png', category='weapon', activity=True, slug='vampiric_burst')
# ])