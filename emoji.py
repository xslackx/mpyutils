class emojis:
    def __init__(self) -> None:
        self.faces = [
            ("smile", "\U0001F600"),
            ("tears_of_joy", "\U0001F602"),
            ("floor_laughing", "\U0001F923"),
            ("loudly_crying", "\U0001F62D"),
            ("blowing_kiss", "\U0001F618"),
            ("smiling_hearts", "\U0001F970"),
            ("smiling_heart-eyes", "\U0001F60D"),
            ("smiling_eyes", "\U0001F60A"),
            ("beaming_smiling_eye", "\U0001F601"),
            ("pleading", "\U0001F97A"),
            ("grinning_sweat", "\U0001F605"),
            ("hugging", "\U0001F917"),
            ("winking", "\U0001F609"),
            ("thinking", "\U0001F914"),
            ("slightly", "\U0001F642"),
            ("flushed", "\U0001F633"),
            ("partying", "\U0001F973"),
            ("smiling_sunglasses", "\U0001F60E"),
            ("pensive", "\U0001F614"),
            ("savoring_face", "\U0001F60B"),
            ("smirking", "\U0001F60F"),
            ("crying", "\U0001F622"),
            ("weary", "\U0001F62B")]
        self.hands = [
            ("raised_hand", "\U0000270B"),
            ("raised_back_of_hand", "\U0001F91A"),
            ("with_fingers_splayed", "\U0001F590"),
            ("waving_hand", "\U0001F44B"),
            ("thumbs_up", "\U0001F44D"),
            ("thumbs_down", "\U0001F44E"),
            ("ok_hand", "\U0001F44C"),
            ("pinching_hand", "\U0001F90F"),
            ("victory_hand", "\U0000270C"),
            ("crossed_fingers", "\U0001F91E"),
            ("call_me_hand", "\U0001F919"),
            ("sign_of_the_horns", "\U0001F918"),
            ("love-you_gesture", "\U0001F91F"),
            ("pointing_left", "\U0001F448"),
            ("pointing_right", "\U0001F449"),
            ("pointing_up", "\U0001F446"),
            ("pointing_down", "\U0001F447"),
            ("index_pointing_up", "\U0000261D"),
            ("right_facing_fist", "\U0001F91C"),
            ("left_facing_fist", "\U0001F91B"),
            ("oncoming_fist", "\U0001F44A"),
            ("clapping_hands", "\U0001F44F"),
            ("raising_hands", "\U0001F64C"),
            ("folded_hands", "\U0001F64F"),
            ("writing_hand", "\U0000270D"),
            ("flexed_biceps", "\U0001F4AA"),
            ("handshake", "\U0001F91D"),
            ("up_together", "\U0001F932"),
            ("heart_hands", "\U0001FAF6"),]
        self.signals = [
            ("antenna_with_bars", "\U0001F4F6"),
            ("no_mobile_phones", "\U0001F4F5"),
            ("mobile_phone_off", "\U0001F4F4"),
            ("vibration_mode", "\U0001F4F3"),
            ("speaker_low_volume", "\U0001F505"),
            ("speaker_medium_volume", "\U0001F506"),
            ("speaker_high_volume", "\U0001F50A"),
            ("speaker_muted", "\U0001F507"),
            ("bell", "\U0001F514"),
            ("bell_with_slash", "\U0001F515"),
            ("loudspeaker", "\U0001F4E2"),
            ("megaphone", "\U0001F4E3"),
            ("warning_sign", "\U000026A0"),
            ("red_circle", "\U0001F534"),
            ("white_circle", "\U000026AA"),
            ("black_circle", "\U000026AB"),
            ("radio_button", "\U0001F518"),
            ("pager", "\U0001F4DF"),
            ("fax_machine", "\U0001F4E0"),
            ("satellite_antenna", "\U0001F4E1"),]
    
    def all_itens(self):
        print(
        {"Faces: ": len(self.faces),
         "Hands: ": len(self.hands),
         "Signals: ": len(self.signals)})
        
    def show_all(self):
        print(self.faces)
        print(self.hands)
        print(self.signals)