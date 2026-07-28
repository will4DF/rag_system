---
title: Image Transformations with imgix
url: https://help.element451.com/en/articles/6963949-image-transformations-with-imgix
collection: Campaigns
---

Apply transformations to images in emails using imgix URL parameters.

# Overview

Images that you upload to Element451 are hosted by a service called **[imgix](https://www.imgix.com/).** imgix is a powerful image management and transformation service that can apply a vast library of edits to an image by appending a parameter to the image’s URL. imgix can apply several simultaneous transformations to images uploaded to E451 Campaigns, such as cropping, resizing, color filters, masking, and more.

This guide discusses the basics of using imgix, presents examples of common transformations, and provides links to additional resources for advanced use.

## Video Guide

---

# How Does it Work?

With imgix transformations, **all edits happen within an image’s URL**. No special tools or editing interface are needed—just add parameters to your image URL.

In Element451, image paths start with `http://451.imgix.net/images/`.

To apply imgix transformation parameters to a URL:

* Append the parameters to the end of the URL after a question mark (?).
* Multiple parameters can be added by separating them with an ampersand (&).

## Click here to view an example

To get started, check out Adam’s headshot uploaded to Element451:

<https://451.imgix.net/training/public/files/K7xnOvgpD82EcOVyYn2J/0Lj6chMrTJ6FakR23WgmVpzb8%253D.png>

I want to add an ellipse mask and resize the image. These transformations will help his email signature look better and load faster.

How do we do this?

1. Append the transformation `?mask=ellipse` to the end of the URL above. This will apply the ellipse mask.
2. Next, I need to add the resize transformation `w=400&h=400` . To do this, I need to combine it with the mask transformation I just added. I do this by adding the `&` between the two. The complete parameter should read as follows:

   `?mask=ellipse&w=400&h=400`.

Take a look at the result here: <https://451.imgix.net/training/public/files/K7xnOvgpD82EcOVyYn2J/0Lj6chMrTJ6FakR23WgmVpzb8%253D.png?mask=ellipse&w=400&h=400>

![](https://downloads.intercomcdn.com/i/o/1084868945/0784daf64c1c8171b291af69/Pro+Tip+-+Orng.png?expires=1784430000&signature=42bf55d8978de5f3e847b1ccd9d87f8e3028a4e8cecd9fc7fa38137e8dce47ff&req=dSAvEsF4lYhbXPMW3Hu4gfCQ1KOtU5fdehOE%2FvBawl4f9T248GHbL0FWALz%2F%0AtQ%3D%3D%0A) Use the imgix [sandbox editor](https://sandbox.imgix.com/create) to upload an image and apply any of the imgix transformations to see what the final image will look like. This is an extremely useful resource to test parameters.

## Click here to view a second example

Let’s look at one of Element451’s default CTA components in the email builder.

[![](https://downloads.intercomcdn.com/i/o/665726975/1fe5251508447f3c80a87967/transformation.gif?expires=1784333700&signature=e350b7e04d9298716ae0b0946e16cdaa65ceed74b4e4bbe6c54ab1dd7931ff6d&req=ciYiEct4lIZaFb4f3HP0gM%2BHqTDhb0XOvPnk70%2Bvfta6sXAEDgvfdJAOFNT%2F%0A4mBikF%2F28186dr0Z7g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/665726975/1fe5251508447f3c80a87967/transformation.gif?expires=1784333700&signature=e350b7e04d9298716ae0b0946e16cdaa65ceed74b4e4bbe6c54ab1dd7931ff6d&req=ciYiEct4lIZaFb4f3HP0gM%2BHqTDhb0XOvPnk70%2Bvfta6sXAEDgvfdJAOFNT%2F%0A4mBikF%2F28186dr0Z7g%3D%3D%0A)

The picture behind the CTA button is a container background image, and the full path of the URL is:

```
https://451.imgix.net/images/email-builder/toa-heftiba.jpeg?blend-color=000000&blend-alpha=50&blend-mode=multiply
```

We can see the imgix transformations that are happening to the right of the “?” symbol in this path.

```
?blend-color=000000&blend-alpha=50&blend-mode=multiply
```

There are several transformations happening at once to this image:

* **blend-color:** specifies the color when applying a blend (set by hex code). In this case #000000 or black.
* **blend-alpha:** changes the alpha (or transparency) of the blend being applied. This is set to 50%. A higher integer (such as 80) would result in a darker image. A smaller integer would result in a lighter (less altered) image.
* **blend-mode:** specifies the blend mode being used. In this case, the blend mode is "multiply," which is used to multiply the color values of overlapping pixels, resulting in a darker image.

---

# Finding Image URLs in Element451

## Campaigns

Using the URL field in the email editor, you can apply transformations to existing components or upload a new image anywhere in the editor and append the imgix parameter to the end of the image path URL. You can find the URL field in the Image Settings.

[![](https://downloads.intercomcdn.com/i/o/665726210/54a668ba7f61122e00b52780/imgix_screenshot.png?expires=1784333700&signature=edfcfefc97a034dde4c23caff44a174927d35916be565b7ba784c0fc8534b72c&req=ciYiEct4n4BfFb4f3HP0gPC8sW%2Fh7NPDJg9AgBNHOeK0rT3AYNftzyL3StKb%0AZ1FOnHY%2BYbnAjt6NeA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/665726210/54a668ba7f61122e00b52780/imgix_screenshot.png?expires=1784333700&signature=edfcfefc97a034dde4c23caff44a174927d35916be565b7ba784c0fc8534b72c&req=ciYiEct4n4BfFb4f3HP0gPC8sW%2Fh7NPDJg9AgBNHOeK0rT3AYNftzyL3StKb%0AZ1FOnHY%2BYbnAjt6NeA%3D%3D%0A)

## Media Manager

You can also find your image URLs in the Media Manager by navigating to **Data + Automations** > **Documents** > **All** **Media**. While you can't edit and save URLs here (images can only be transformed in Campaigns), this is great place to grab URLs to practice adding parameters like we did in the [example above](#h_69aba7bbf1).

---

# Clearing Transformations

When using transformations in a Campaign, you can restore an image to its original state by clicking the **"clear transformations"** button next to the image URL field.   
​

[![](https://downloads.intercomcdn.com/i/o/665738101/1264600bedaa58babf1b47cf/clear_transformation.png?expires=1784333700&signature=36058b3d0e000077c838c4e52d16393e4a84762e8f194ab624916d48bc4b7d96&req=ciYiEcp2nIFeFb4f3HP0gE3J3Ylp3c0MQpqm8R1%2B47JO6E2q4YWJqpl9ILL4%0AJmOIhp5q2f%2BR2FmGLw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/665738101/1264600bedaa58babf1b47cf/clear_transformation.png?expires=1784333700&signature=36058b3d0e000077c838c4e52d16393e4a84762e8f194ab624916d48bc4b7d96&req=ciYiEcp2nIFeFb4f3HP0gE3J3Ylp3c0MQpqm8R1%2B47JO6E2q4YWJqpl9ILL4%0AJmOIhp5q2f%2BR2FmGLw%3D%3D%0A)

---

# Common Transformations with Examples

## Resize Fit

[Resize fit](https://docs.imgix.com/apis/rendering/size/fit) can be used to resize an image based on different types of parameters. Set your image dimensions using pixel values for width and height.  
​

```
?fit=crop&w=WIDTHVALUE&h=HEIGHTVALUE  
  
Example:  
?fit=crop&w=400&h=400
```

[![](https://downloads.intercomcdn.com/i/o/667046410/b8a9b5c9d9402c5ec378efad/crop.gif?expires=1784333700&signature=1af5e0fdfd1cd37b581ff03f4a9699ae51ce35ca778a76b1d94ef73193be2cd3&req=ciYgFs14mYBfFb4f3HP0gA3o399u8zxEdz5sebErqEI27lc21WgfhyjVnayC%0AiasvvihbSTupZRPg%2Bw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/667046410/b8a9b5c9d9402c5ec378efad/crop.gif?expires=1784333700&signature=1af5e0fdfd1cd37b581ff03f4a9699ae51ce35ca778a76b1d94ef73193be2cd3&req=ciYgFs14mYBfFb4f3HP0gA3o399u8zxEdz5sebErqEI27lc21WgfhyjVnayC%0AiasvvihbSTupZRPg%2Bw%3D%3D%0A)

## Face Detection

[Face detection](https://docs.imgix.com/apis/rendering/face-detection) can be used to center on any faces within an image automatically. This is especially useful for profile photos. Use the "fit=crop" parameter to specify the final image dimensions and the "facepad" parameter to set the padding around the subject in the image.

```
?w=WIDTHVALUE&h=HEIGHTVALUE&fit=facearea&facepad=PADDINGVALUE  
  
Example:  
?w=400&h=400&fit=facearea&facepad=3
```

[![](https://downloads.intercomcdn.com/i/o/667059077/bea000b81afc235cdf59ee41/face_crop.gif?expires=1784333700&signature=1594b5f8bf963b89edd2c40a460daab1b3eb95b7fd02be4d4681f68ca56b5bdf&req=ciYgFsx3nYZYFb4f3HP0gG%2B4SGWLORd44P7N1BasCCQzQucDdVSnguCMHLeq%0AuWnyK%2F7r4a0MYlOgVA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/667059077/bea000b81afc235cdf59ee41/face_crop.gif?expires=1784333700&signature=1594b5f8bf963b89edd2c40a460daab1b3eb95b7fd02be4d4681f68ca56b5bdf&req=ciYgFsx3nYZYFb4f3HP0gG%2B4SGWLORd44P7N1BasCCQzQucDdVSnguCMHLeq%0AuWnyK%2F7r4a0MYlOgVA%3D%3D%0A)

##

## Masks (e.g., ellipse)

[Masks](https://docs.imgix.com/apis/rendering/mask) can be applied for several shapes (including custom shapes). The most common use case of the mask parameter is for an ellipse transformation.   
​

```
?mask=ellipse&w=WIDTHVALUE&h=HEIGHTVALUE  
  
Example:  
?mask=ellipse&w=400&h=400
```

[![](https://downloads.intercomcdn.com/i/o/667064882/15379cf10ce1859539c6b837/ellipse.gif?expires=1784333700&signature=8123572081198e1139e90fd58c466defaec83cba850a0257cdce618bee406ba3&req=ciYgFs96lYldFb4f3HP0gCCeqDmoHq8al7%2FP5cQ3c0%2Byw08DPffmRb0BwCQR%0AIgjOjBW6Hf%2FSPnuMfg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/667064882/15379cf10ce1859539c6b837/ellipse.gif?expires=1784333700&signature=8123572081198e1139e90fd58c466defaec83cba850a0257cdce618bee406ba3&req=ciYgFs96lYldFb4f3HP0gCCeqDmoHq8al7%2FP5cQ3c0%2Byw08DPffmRb0BwCQR%0AIgjOjBW6Hf%2FSPnuMfg%3D%3D%0A)

## Rotations

[Rotations](https://docs.imgix.com/apis/rendering/rotation/rot) are simple transformations to rotate the image according to the value specified (0-360 degrees).

```
?rot=ROTATIONVALUE  
  
Example:  
?rot=90
```

[![](https://downloads.intercomcdn.com/i/o/667067320/0c991b06d7da10eee03cb801/rotatation.gif?expires=1784333700&signature=4aad5b535a2cafeda89b097c1de7de200519f4ea7701e772ec786d8a3a553cb6&req=ciYgFs95noNfFb4f3HP0gNhUh7v0%2Bo4Q1htSbxATg7ynu9m4UN%2FfUoqYYg%2FY%0AUWYdcXvnaA1F2Bhy4Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/667067320/0c991b06d7da10eee03cb801/rotatation.gif?expires=1784333700&signature=4aad5b535a2cafeda89b097c1de7de200519f4ea7701e772ec786d8a3a553cb6&req=ciYgFs95noNfFb4f3HP0gNhUh7v0%2Bo4Q1htSbxATg7ynu9m4UN%2FfUoqYYg%2FY%0AUWYdcXvnaA1F2Bhy4Q%3D%3D%0A)

## Blend Mode

[Blend mode](https://docs.imgix.com/apis/rendering/blending/blend-mode) is a powerful transformation that can be used for several use cases, the most common being lightening or darkening an image or applying a color filter.

**Lighten**

```
?blend-mode=screen&blend-color=COLORHEXCODE&blend-alpha=AMOUNT  
  
Example:  
?blend-mode=screen&blend-color=FFFFFF&blend-alpha=80
```

**Darken**

```
?blend-mode=multiply&blend-color=COLORHEXCODE&blend-alpha=AMOUNT  
  
Example:  
?blend-mode=multiply&blend-color=000000&blend-alpha=80
```

**Color Filter**

```
?blend-mode=multiply&blend-color=COLORHEXCODE&blend-alpha=AMOUNT  
  
Example:  
?blend-mode=multiply&blend-color=c95f08&blend-alpha=80
```

---

# Additional imgix Resources

imgix maintains a robust library of documentation with tips and tutorials, a full codex with examples for all of the available transformations, and a sandbox tool for testing.

* [Tutorials](https://docs.imgix.com/tutorials)
* [Transformation Codex](https://docs.imgix.com/apis/rendering)
* [Sandbox Editor](https://sandbox.imgix.com/create)

---