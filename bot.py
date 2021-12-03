import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token


from vktools import Keyboard, ButtonColor, Text, OpenLink, Location, Carousel, Element

vk = vk_api.VkApi(token=token)


def send_message(user_id, message, keyboard=None, carousel=None):
	values = {
		"user_id": user_id,
		"message": message,
		"random_id": 0
	}

	if keyboard is not None:
		values["keyboard"] = keyboard.add_keyboard()
	if carousel is not None:
		values["template"] = carousel.add_carousel()

	vk.method("messages.send", values)


for event in VkLongPoll(vk).listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text.lower()
		user_id = event.user_id

		if text == "test":
			keyboard = Keyboard(
				[
					[
						Text("RED", ButtonColor.NEGATIVE),
						Text("GREEN", ButtonColor.POSITIVE),
						Text("BLUE", ButtonColor.PRIMARY),
						Text("WHITE")
					],
					[
						OpenLink("YouTube", "https://youtube.com/c/Фсоки"),
						Location()
					]
				]
			)

			send_message(user_id, "VkTools Keyboard by DevOps ~", keyboard)

		elif text == "test carousel":
			carousel = Carousel(
				[
					Element(
						"Title 1",
						"Description 1",
						"-209284522_457239019", # photo_id
						"https://vk.com/club209284522", # redirect url, if user click on element
						[Text("Button 1", ButtonColor.POSITIVE)]
					),
					Element(
						"Title 2",
						"Description 2",
						"-209284522_457239019", # photo_id
						"https://vk.com/club209284522", # redirect url, if user click on element
						[Text("Button 2", ButtonColor.PRIMARY)]
					)
				]
			)

			send_message(user_id, "VkTools Carousel by DevOps ~", carousel=carousel)