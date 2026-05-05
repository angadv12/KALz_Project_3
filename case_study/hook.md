# Hook Document



## Can You Catch an AI Image Before It Spreads?



Imagine the Cavalier Daily receives two images tied to a breaking campus story. One came from a real photo source. The other came from a generative model. Both look believable at a glance, and the newsroom needs an evidence-based call before the image moves across group chats and social media.

You are the analyst on that first pass. Your job is not to build a perfect truth machine. Your job is to test whether a reproducible computer-vision workflow can separate real images from AI-generated images better than a person scanning pixels by eye.

The KALz project gives you a starting point: the CIFAKE dataset, a clean repository, two pretrained CNN models, saved evaluation outputs, and Grad-CAM examples. CIFAKE contains 120,000 low-resolution images split evenly between REAL images from CIFAR-10 and FAKE images generated to match that style. The original project compared ResNet-50 and DenseNet-121. Both models beat the 80 percent target and the 92.98 percent CIFAKE paper baseline, with DenseNet-121 reaching 96.97 percent test accuracy.

Your mission is to turn that project into a short, honest technical brief for a non-expert reader. You will explain the problem, run or inspect the workflow, compare the models, and decide what the results do and do not prove. The strongest answer will pair metrics with skepticism: confusion matrices show where the model failed, and Grad-CAM helps you ask whether the model focused on meaningful image regions or dataset-specific artifacts.

By the end, you should be able to answer one practical question: if someone handed you a suspicious image, what evidence would make you trust or doubt a CNN-based detector?

